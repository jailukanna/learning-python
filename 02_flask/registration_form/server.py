# import dependencies and setup Flask application:
from flask import Flask, render_template, request, redirect, flash
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'  # secret key required for flash messaging (because it uses session)

# setup root route:
@app.route('/')
def index():
    print "Loading index page..."
    return render_template('index.html')

# setup form submission route:
@app.route('/register', methods=['POST'])
def register():
    print "New user registration detected...", "Validating..."
    # Begin Validations:
    # Check if any fields are blank:
    if ((len(request.form['email']) < 1) or (len(request.form['first_name']) < 1) or (len(request.form['last_name']) < 1) or (len(request.form['password']) < 1) or (len(request.form['confirm_password']) < 1)):
        print "Error: All fields are required."
        flash("All fields are required.", "error")
        return redirect('/')
    # Check if first name or last name contain any numbers (I've also included to check if it contains any characaters):
    # Define our regex pattern:
    # Note: This pattern matches for anything which is *not* contained in
    # the defined set of characters below (the second carrot `^` denotes
    # a *not* grouping)
    num_regex = re.compile(r'^[^0-9~`!@#$%^&*()_+=\-\{\}:;"\'<,>.?/]*$')
    # Check for matches with our first and last names:
    if not num_regex.match(request.form['first_name']) or not num_regex.match(request.form['last_name']):
        print "Error: First name and last name may contain only letters."
        flash("First and last names may contain only letters.", "error")
        return redirect('/')
    # Check if password is 8 characters or less:
    if ((len(request.form['password']) <= 8) or (len(request.form['confirm_password']) <= 8)):
        print "Error: Password must be greater than 8 characters."
        flash("Password must be greater than 8 characters.", "error")
        return redirect('/')
    # Check if password and confirm password match:
    if request.form['password'] != request.form['confirm_password']:
        print "Error: Password and confirmation do not match."
        flash("Password and confirmation must match.", "error")
        return redirect('/')
    # Check if email is valid format:
    # Define our regex pattern:
    email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if not email_regex.match(request.form['email']):
        print "Error: Email is not a valid format."
        flash("Email must be in a valid format.", "error")
        return redirect('/')
    # Because each failed validation returns a redirect,
    # this area will not run unless all validations have passed:
    print "Validations passed."
    print "Registering user now..."
    # Flash message a success message, notice the second parameter (which can be named anything).
    # This is then used in the View to filter for that same category (in this case, `success`)
    # If a second parameter is not given, (like in the examples above), the default cateogry is `message`
    # See for more details on message categorization: http://flask.pocoo.org/docs/0.10/patterns/flashing/#flashing-with-categories
    flash(u"User registration successful.", "success")
    return redirect('/')

# run app and setup debug mode:
app.run(debug=True)
