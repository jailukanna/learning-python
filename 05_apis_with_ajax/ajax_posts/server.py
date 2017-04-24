from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
from datetime import datetime
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector

#CONSTANTS
app = Flask(__name__)
'''
Set variable 'mysql' to be an instance of the MySQLConnector class,
taking our entire application as the first argument and the database
name as the second argument.
'''
mysql = MySQLConnector(app, 'ajax_posts')

#ROUTES
@app.route('/')
def index():
	query = "SELECT * FROM posts"
	notes = mysql.query_db(query)
	return render_template('index.html', notes=notes)

@app.route('/notes/index_json')
def index_json():
    query = "SELECT * FROM posts"
    notes = mysql.query_db(query)
    return jsonify(notes=notes)

@app.route('/create', methods=['POST'])
def create():
	note = request.form
	data = {'description' : note['description']}
	query = "INSERT INTO posts(description, created_at, updated_at) VALUES(:description, NOW(), NOW());"
	mysql.query_db(query,data)
	return_query = "SELECT * FROM posts;"
	notes = mysql.query_db(return_query)
	return render_template('/partials/index.html', notes=notes)

#RUN AND DEBUG
app.run(debug=True)
