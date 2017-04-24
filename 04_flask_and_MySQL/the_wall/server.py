# Login and Registration Assignment - Tim Knab - Coding Dojo - August 2016

#APP DEPENDANCIES
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector 
from flask.ext.bcrypt import Bcrypt
import re
import datetime
from datetime import datetime
from datetime import timedelta

#CONSTANTS
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall')
app.secret_key = '4c832cbbe993f988cfb877f4322d137d'
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
LETTERS_REGEX = re.compile(r'^[A-Za-z]+$')

#SQL QUERIES
queries = {
	'createUser' : 'INSERT INTO users (first_name, last_name, email, pwd_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pwd_hash, NOW(), NOW());',
	'getEmail' : 'SELECT * FROM users WHERE email = :email LIMIT 1;',
	'getUserId' : 'SELECT * FROM users WHERE id = :id;',
	'createPost' : 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW());',
	'showPosts' : 'SELECT messages.id, CONCAT(users.first_name," ",users.last_name) AS name, messages.message, messages.user_id, messages.created_at FROM messages LEFT JOIN users ON messages.user_id=users.id;',
	'createComment' : 'INSERT INTO comments (message_id, user_id, comment, created_at, updated_at) VALUES (:message_id, :user_id, :comment, NOW(), NOW());',
	'showComments' : 'SELECT CONCAT(users.first_name," ",users.last_name) AS name, comments.id AS comments_id, comments.comment, comments.message_id AS comments_message_id, messages.id AS message_id, comments.created_at FROM comments LEFT JOIN messages ON comments.message_id=messages.id LEFT JOIN users ON comments.user_id=users.id;',
	'deletePost' : 'DELETE FROM comments WHERE message_id= :id; DELETE FROM messages WHERE id= :id;',
	'getPost' : 'SELECT * FROM messages WHERE id= :id;',
	'updatePost' : 'UPDATE messages SET message=:message, updated_at=NOW() WHERE id = :id;'
}

#HELPER FUNCTIONS
def regexEmail(email):
	return EMAIL_REGEX.match(email)

def regexLetters(str):
	return LETTERS_REGEX.match(str)

def print_flash_messages(message_list):
	for message in message_list:
		flash(message)

def generateHash(userPassword):
	password = userPassword
	pwd_hash = bcrypt.generate_password_hash(password)
	return pwd_hash

def registrationValidation(form):
	errors = []
	if len(form['first_name']) < 1 or len(form['last_name']) < 1 or len(form['email']) < 1 or len(form['password']) < 1 or len(form['password_confirm']) < 1:
		errors.append('All fields must be filled out to register.')
	else:
		if len(form['first_name']) < 2 or len(form['first_name']) < 2:
			errors.append('First and Last name must be more than two (2) characters.')
		if regexEmail(form['email']) is None:
			errors.append('Email must be in a valid format.')
		if regexLetters(form['first_name']) is None or regexLetters(form['last_name']) is None:
			errors.append('First and last name must be letters only.')
		if len(form['password']) < 8:
			errors.append('Password must be at least 8 characters long.')
		if form['password'] != form['password_confirm']:
			errors.append('Your password and confirmation password do not match.')
		checkExistingUser = mysql.query_db(queries['getEmail'], {'email' : form['email']})
		if not checkExistingUser:
			pass		
		else:
			errors.append('A user with that email address already exists.')
	return errors

def loginValidation(form):
	errors = []
	if len(form['loginEmail']) < 1 or len(form['loginPassword']) < 1:
		errors.append('A username and password is required to login.')
	else:
		if regexEmail(form['loginEmail']) is None:
			errors.append('Email address must be in a valid format.')
		if len(form['loginPassword']) < 8:
			errors.append('Password must be at least 8 characters long.')
		try:
			user = mysql.query_db(queries['getEmail'], {'email': form['loginEmail']})[0]
			if bcrypt.check_password_hash(user['pwd_hash'], form['loginPassword']):
				session['loggedInUser'] = user['id']
			else:
				errors.append('Password for that username is incorrect.')
		except IndexError:
			pass
			errors.append('There is no record for that email address.')
	return errors

def postValidation(form):
	errors = []
	if len(form['message']) < 1:
		errors.append('Please enter a message.')
	return errors

#ROUTES
@app.route('/', methods=["GET"])
def index():
	try:
		session['loggedInUser']
		query = [queries['getUserId'], queries['showPosts'], queries['showComments']]
		data = [{ 'id' : unicode(session['loggedInUser']) }, {}, {}]
		loggedInUser = mysql.query_db(query[0], data[0])[0]
		messageList = mysql.query_db(query[1], data[1])
		commentList = mysql.query_db(query[2], data[2])
		now = datetime.now()
		thirtyMinutes = timedelta(minutes=30)
		return render_template ('wall.html', loggedInUser=loggedInUser, messageList=messageList, commentList=commentList, now=now, thirtyMinutes=thirtyMinutes)
	except:
		return render_template('index.html')

@app.route('/register', methods=["POST"])
def userRegister():
	errors = registrationValidation(request.form)
	if len(errors) > 0:
		print_flash_messages(errors)
		return redirect('/')
	else:
		pwd_hash = generateHash(request.form['password']) 
		query = [queries['createUser'], queries['getEmail']]
		data = {
			'first_name' : request.form['first_name'],
			'last_name' : request.form['last_name'],
			'email' : request.form['email'],
			'pwd_hash' : unicode(pwd_hash)
		}
		mysql.query_db(query[0], data)
		user = mysql.query_db(query[1], data)[0]
		session['loggedInUser'] = user['id']
		return redirect('/')

@app.route('/login', methods=["POST"])
def userLogin():
	errors = loginValidation(request.form) #validates fields and checks password
	if len(errors) > 0:
		print_flash_messages(errors)
		return redirect('/')
	else:
		query = queries['getEmail']
		data = { 'email' : request.form['loginEmail'] }
		user = mysql.query_db(query, data)[0]
		session['loggedInUser'] = user['id']
		return redirect('/')

@app.route('/post', methods=["POST"])
def createPost():
	errors = postValidation(request.form)
	if len(errors) > 0:
		print_flash_messages(errors)
		return redirect('/')
	else:
		query = queries['createPost']
		data = {
			'user_id' : session['loggedInUser'],
			'message' : request.form['message']
		}
		mysql.query_db(query, data)
		flash('Post has been created!')
		return redirect('/')

@app.route('/post/<id>/delete', methods=['POST'])
def deletePost(id):
	query = queries['deletePost']
	data = {
		'id' : id
	}
	mysql.query_db(query, data)
	flash('Message has been deleted!')
	return redirect('/')

@app.route('/post/<id>/edit', methods=['POST'])
def editPost(id):
	query = [queries['getPost'], queries['getUserId'], queries['getPost']]
	data = [{'id' : id }, {'id' : unicode(session['loggedInUser'])}, {'id' : id}]
	user = mysql.query_db(query[0], data[0])[0]
	loggedInUser = mysql.query_db(query[1], data[1])[0]
	messageList = mysql.query_db(query[2], data[2])
	return render_template('edit.html', user=user, loggedInUser=loggedInUser, messageList=messageList)

@app.route('/post/<id>/update', methods=['POST'])
def updatePost(id):
	query = queries['updatePost']
	data = {
		'id' : id,
		'message' : request.form['message'],
	}
	mysql.query_db(query, data)
	flash('Your message has been updated!')
	return redirect('/')

@app.route('/comment/<id>', methods=["POST","GET"])
def createComment(id):
	query = queries['createComment']
	data = {
		'message_id' : id,
		'user_id' : session['loggedInUser'],
		'comment' : request.form['comment' + id] 
	}
	if len(data['comment']) <= 0:  #validates for non-empty comment
		flash('Please enter a comment.')
		return redirect('/')
	else:
		mysql.query_db(query, data)
		flash('Comment has been created!')
		return redirect('/')

@app.route('/logout', methods=["GET"])
def userLogOut():
	session.pop('loggedInUser', None)
	flash('You\'ve been logged out!')
	return redirect('/')

#RUN APP AND DEBUG
app.run(debug=True)
