'''
This assignment was pretty tricky. Some things to keep in mind about this assignment:

    1. We use Regex here, thus we have to 'import re' to make sure we bring in the regex library
    2. Regex can be a little confusing, make sure you understand the characaters we're using and what they pertain to
    3. Make sure you understand the difference between re.compile() and re.match()
    4. Note: when we ran re.match(), we already compiled as a variable, 'email_regex', thus we can use email_regex.match() as the command
    5. Note: we used a secret key for this app
    6. Note: The use of flash - note the use of get_flashed_messages on index.html (http://flask.pocoo.org/docs/0.11/patterns/flashing/)
    7. Note: We also use get_flashed_messages on success.html
    8. Note: When we run our remove(id) function at the bottom (our delete), 'id' is being gathered from a for loop as record['id']
    9. Note: The use of dictionaries and our initial setup. Note how we use flash messages to make life easier. These two aspects are ways that you can improve upon your current code attempts and is more advanced, along with the use of regex this was a great assignment.
    10. Note: 'success.html' tempate, notice the use of: strftime('%d/%m/%y %I:%M%p') and the formatting and what exactly it's doing
'''


# dependancies
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re # import regex


# app, db and constants
app = Flask(__name__)
mysql = MySQLConnector(app,'email')
app.secret_key = 'some_long_secret_key_or_hashtag'
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')   # you have to use re.compile() - once this is done, you can use match(). resource to http://regexr.com/

# setup a dictionary of our sql queries
queries = {
    'create' : "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW());", # ':email_address denotes dictionary value for key 'email_adress', ie ':email_address' for  dictionary pair ' email_adress: "something" ' would be the string, "something"
    'index' : "SELECT * FROM emails",
    'delete' : "DELETE FROM emails WHERE id = :id"
}

# build a function we'll use to evaluate regex
def validateEmail(email):
    return EMAIL_REGEX.match(email)

# index route
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":

        if(validateEmail(request.form['email'])):
            query = queries['create']
            data = { 
                'email_address': request.form['email']
            }
            mysql.query_db(query, data)
            flash('Success! ' + data['email_address'] +' accepted and database record created!')
            return redirect('/success')

        else:
            flash('Please double check your email format, email not valid!')

    return render_template('index.html')

# success route
@app.route('/success', methods=["GET"])
def success():
    query = queries['index']
    data = {}
    emails = mysql.query_db(query, data)
    return render_template('success.html', emails=emails)

# delete route
@app.route('/<id>', methods=["POST"])
def remove(id):
    query = queries['delete']
    data = { 'id':id } # the second variable, id, will be whatever is gathered from the record
    flash('Email deleted!')
    mysql.query_db(query,data)
    return redirect('/success')


app.run(debug=True)