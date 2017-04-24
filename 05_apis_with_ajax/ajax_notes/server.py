from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
from datetime import datetime
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector

#CONSTANTS
app = Flask(__name__)
mysql = MySQLConnector(app, 'ajax_notes')

#ROUTES
@app.route('/')
def index():
	notes = mysql.query_db("SELECT * FROM notes")
	return render_template('index.html', notes=notes)

@app.route('/notes/index_json')
def index_json():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    print notes
    return jsonify(notes=notes)

@app.route('/notes/create', methods=['POST'])
def create():
	query = "INSERT INTO notes(title, created_at, updated_at) VALUES(:title, NOW(), NOW());"
	data = {'title' : request.form['title']}
	print data['title']
	mysql.query_db(query,data)
	return redirect('/notes')

@app.route('/notes/<id>/destroy', methods=['GET'])
def destroy(id):
	query = "DELETE FROM notes WHERE id= :id;"
	data = {'id' : id}
	print data['id']
	mysql.query_db(query,data)
	return redirect('/notes')

@app.route('/notes/<id>/update', methods=['POST'])
def update(id):
	query = "UPDATE notes SET description=:description, updated_at=NOW() WHERE id=:id;"
	data = {
		'description' : request.form['description'],
		'id' : id
	}
	print data
	mysql.query_db(query,data)
	return redirect('/notes')

@app.route('/notes')
def notes():
	query = "SELECT * FROM notes;"
	notes = mysql.query_db(query)
	print notes
	return render_template('/partials/notes.html', notes=notes)

#RUN AND DEBUG
app.run(debug=True)
