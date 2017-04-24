from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector
app = Flask(__name__)
'''
Set variable 'mysql' to be an instance of the MySQLConnector class,
taking our entire application as the first argument and the database
name as the second argument.
'''
mysql = MySQLConnector(app, 'quotes_api')

@app.route('/quotes')
def index():
	query = "SELECT * FROM quotes"
	quotes = mysql.query_db(query)
	return render_template('index.html', quotes=quotes)

@app.route('/quotes/index_json')
def index_json():
    query = "SELECT * FROM quotes"
    quotes = mysql.query_db(query)
    return jsonify(quotes)

@app.route('/quotes/create', methods=['POST'])
def create():
	query = "INSERT INTO quotes(quote, author) VALUES('{}','{}');".format(request.form['quote'], request.form['author'])
	mysql.query_db(query)
	return_query = "SELECT * FROM quotes"
	quotes = mysql.query_db(return_query)
	return render_template('partials/index.html', quotes=quotes)

app.run(debug=True)
