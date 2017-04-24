# import dependencies and setup Flask application:
from flask import Flask, render_template, request, redirect, flash
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'  # secret key required for flash messaging (because it uses session)

# setup root route:
@app.route('/')
def index():
    return render_template('index.html')

# setup route for handling survey:
@app.route('/result', methods=['POST'])
def result():
    #######################
    #--CAPTURE FORM DATA--#
    #######################
    # Capture form data as a dictionary:
    data = {
        "name" : request.form['name'],
        "email" : request.form['email'],
        "location" : request.form['location'],
        "language" : request.form['language'],
        "comment" : request.form['comment'],
    }

    # Just a color test:
    colors = {
        "R" : 'red',
        "B" : 'blue',
        "P" : 'purple',
    }

    # Print statement for developer check:
    print "/////////"
    if 'comment' in data:
        print data['comment']
    print "/////////"

    ######################
    #-----VALIDATIONS----#
    ######################
    email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

    # check if name or comments fields are empty:
    if ((len(data['name']) < 1) or (len(data['comment']) < 1) or (len(data['email']) < 1)):
        print "Name, comment and email fields must not be blank."
        flash("Name, comment and email fields must not be blank.")
        return redirect('/')
    # check if comments field is greater than 120 characters:
    elif len(data['comment']) > 120:
        print "Comments must be less than 120 characters long."
        flash("Comments must be less than 120 characters long.")
        return redirect('/')
    # check if email passes regex check:
    elif not email_regex.match(data['email']):
        print "Email did not pass regex validation."
        flash("Email address must be a valid format.")
        return redirect('/')
    # Render results page and send along form data:
    return render_template('results.html', data = data, colors = colors)

# run app and setup debug mode:
app.run(debug=True)
