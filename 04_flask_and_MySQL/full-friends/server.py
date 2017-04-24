# full friends assignment - Tim Knab - Coding Dojo - August 2016

# DEPENDANCIES 
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re # import regex

# CONSTANTS
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriends')
app.secret_key = 'a552d364870644687f4d095783af2e8a'
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

# SQL QUERIES
queries = {
    'create' : "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());", # ':email_address denotes dictionary value for key 'email_adress', ie ':email_address' for  dictionary pair ' email_adress: "something" ' would be the string, "something"
    'index' : "SELECT * FROM friends",
    'show' : "SELECT * FROM friends WHERE id = :id",
    'delete' : "DELETE FROM friends WHERE id = :id",
    'update' : "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :id"
}

# FORM VALIDATION FUNCTIONS
def validateEmail(email):
    return EMAIL_REGEX.match(email)

# ROUTES
# root
@app.route('/', methods=["GET","POST"])
def index():
	friendsList = mysql.query_db(queries['index'], {})
	return render_template('index.html', friendsList=friendsList)

# create friend
@app.route('/friends', methods=["POST"])
def create():
	if validateEmail(request.form['email']) is not None:
		query = queries['create']
		data = {
			'first_name' : request.form['first_name'],
			'last_name' : request.form['last_name'],
			'email' : request.form['email']
			}
		mysql.query_db(query, data)
		flash('Success! ' + data['first_name'] + ' ' + data['last_name'] + ' has been created in the database!')
		return redirect('/')
	else:
		flash('Please enter a valid email address.')
		return redirect('/')


# edit friend
@app.route('/friends/<id>/edit', methods=["GET"])
def edit(id):
	query = queries['show']
	data = {
		'id' : id
	}
	showFriend = mysql.query_db(query, data)[0] # the '[0] will give us a dictionary back instead of a list'
	print showFriend
	return render_template('edit.html', showFriend=showFriend)

# update friend
@app.route('/friends/<id>', methods=["POST"])
def update(id):
	if validateEmail(request.form['email']) is not None:
		query = queries['update']
		data = {
			'first_name' : request.form['first_name'],
			'last_name' : request.form['last_name'],
			'email' : request.form['email'],
			'id' : id
			}
		mysql.query_db(query, data)
		flash('User ' + data['first_name'] + ' ' + data['last_name'] + ' has been updated in the database!')
		return redirect('/')
	else:
		flash('Please enter a valid email address.')
		return redirect('/')

# delete friend
@app.route('/friends/<id>/delete', methods=["POST"])
def destroy(id):
	query = queries['delete']
	data = {
		'id' :id
	}
	flash('Email Deleted!')
	mysql.query_db(query, data)
	return redirect('/')

# RUN APP AND DEBUG
app.run(debug=True)