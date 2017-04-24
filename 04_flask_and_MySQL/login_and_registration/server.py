# Login and Registration Assignment - Tim Knab - Coding Dojo - August 2016

#APP DEPENDANCIES
from flask import Flask, request, redirect, render_template, session, flash #routes, session, flash
from mysqlconnection import MySQLConnector  #for database
from flask.ext.bcrypt import Bcrypt #for pw encrpytion
import re #for regex

#CONSTANTS
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_registration')
app.secret_key = '3c832cbae883f988cfb877f4322d137c'
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
LETTERS_REGEX = re.compile(r'^[A-Za-z]+$')

#QUERIES
queries = {
    'create_user' : "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW());",
    'get_email'	: "SELECT * FROM users WHERE email = :email LIMIT 1",
    'get_id' : "SELECT * FROM users WHERE id = :id",
}

#VALIDATION AND FLASH HELPER FUNCTIONS
def regexEmail(email):
	return EMAIL_REGEX.match(email)

def regexLetters(str):
	return LETTERS_REGEX.match(str)

def validate_registration(form_info):
	errors = []
	if len(form_info['first_name']) < 2 or len(form_info['last_name']) < 2:
		errors.append('First name and last name must be at least 2 characters.')
	if regexLetters(form_info['first_name']) is None or regexLetters(form_info['last_name']) is None:
		errors.append('First and last name must contain letters only.')
	if regexEmail(form_info['email']) is None or len(form_info['email']) < 1:
		errors.append('Please enter an email in a valid format.')
	else:
		query = queries['get_email']
		data = { 'email' : form_info['email'] }
		existingUser = mysql.query_db(query, data)
		if not existingUser:
			pass
		else:
			errors.append('A user with this email address already exists.')
	if len(form_info['password']) < 8 or form_info['password'] != form_info['password_confirm'] or len(form_info['password']) < 1:
		errors.append('Passwords must match and be at least 8 characters in length.')
	return errors

def validate_login(form_info):
	errors = []
	query = queries['get_email']
	data = { 'email' : form_info['email'] }
	password = form_info['password']
	if regexEmail(form_info['email']) is None or len(form_info['email']) < 1:
		errors.append('Please enter an email in a valid format.')
	if len(form_info['password']) < 1:
		errors.append('You must enter a password.')
	try:
		user = mysql.query_db(query, data)[0]
		if bcrypt.check_password_hash(user['pw_hash'], password):
			session['loggedIn'] = user['id']
		else:
			errors.append('Password for that username is incorrect.')
	except IndexError:
		pass
		errors.append('There is no record for that email address. Please register before logging in.')
	return errors

def print_flash_messages(message_list):
	for message in message_list:
		flash(message)

#ROOT ROUTE
@app.route('/', methods=["GET"])
def index():
	if session.get('loggedIn') is not None:
		query = queries['get_id']
		data = { 'id' : session['loggedIn'] }
		user = mysql.query_db(query, data)[0]
		return render_template('success.html', user=user)
	else:
		return render_template('index.html')

#REGISTER USER ROUTE
@app.route('/success', methods=["POST"])
def createUser():
	potential_errors = validate_registration(request.form)
	if len(potential_errors) > 0:
		print_flash_messages(potential_errors)
		return redirect('/')
	else:
		password = request.form['password']
		password_confirm = request.form['password_confirm']
		pw_hash = bcrypt.generate_password_hash(password)
		query = queries['create_user']
		data = {
			'first_name' : request.form['first_name'],
			'last_name'	: request.form['last_name'],
			'email'	: request.form['email'],
			'pw_hash' : pw_hash
		}
		mysql.query_db(query, data)
		user = mysql.query_db(queries['get_email'], data)[0]
		session['loggedIn'] = user['id']
		return render_template('success.html', user=user)

#LOGIN ROUTE
@app.route('/login', methods=["GET", "POST"])
def login():
	login_errors = validate_login(request.form)
	if len(login_errors) > 0:
		print_flash_messages(login_errors)
		return redirect('/')
	else:
		query = queries['get_email']
		data = { 'email': request.form['email'] }
		user = mysql.query_db(query, data)[0] # user will be returned in a list
		return render_template('success.html', user=user)

#LOGOUT ROUTE
@app.route('/logout')
def logout():
	session.pop('loggedIn', None)
	flash('You\'ve been successfully logged out!')
	return redirect('/')

#RUN APP AND DEBUG
app.run(debug=True)