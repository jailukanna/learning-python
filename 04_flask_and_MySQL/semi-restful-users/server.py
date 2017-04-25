#------------------------------------------#
#----- Setup Application Dependencies -----#
#------------------------------------------#
from flask import Flask, request, redirect, render_template, session, flash # project dependencies
from mysqlconnection import MySQLConnector # mysql connection file
import re # regex

#-------------------------------#
#----- Setup App Variables -----#
#-------------------------------#
app = Flask(__name__) # setup Flask application
mysql = MySQLConnector(app,'semi_restful_users') # connect Flask app to DB, 'semi_restful_users'
app.secret_key = 'a552d364870644687fAdDdf#95783af2e8a' # setup Secret Key

#--------------------------------------------#
#----- Setup Dictionary for SQL Queries -----#
#--------------------------------------------#
# CRUD queries for use in our routes below:
queries = {
    'create' : "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());", # ':email_address denotes dictionary value for key 'email_adress', ie ':email_address' for  dictionary pair ' email_adress: "something" ' would be the string, "something"
    'index' : "SELECT * FROM users",
    'show' : "SELECT * FROM users WHERE id = :id",
    'delete' : "DELETE FROM users WHERE id = :id",
    'update' : "UPDATE users SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :id"
}

#------------------------#
#----- Setup Routes -----#
#------------------------#
# Show All Users, or, if `POST` request method, Create New User:
@app.route('/users', methods=["GET","POST"])
def users():
    '''
    This route either gets all users, or creates a user, depending upon if the
    request method is a 'GET' or a 'POST', respectively.
    '''
    # Check if request method is `POST` (via form submission):
    if request.method == 'POST':
        # If so, query database and make new User:
        print 'Post method detected. Creating user now!'
        # Query format: `mysql.query_db(<query>, <dictionary-data>)`
        # Note: Because our `mysqlconnection.py` file returns only
        # an index value for any `INSERT` SQL queries, our returned
        # data in the below circumstance is only an `id`, thus the
        # variable naming.
        new_user_id = mysql.query_db(queries['create'], {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        })
        print '////////'
        print new_user_id
        print '////////'
        # Then, load user view page after user is created:
        return redirect('/users/' + str(new_user_id))

    # If request method is get (default), get all users
    users_list = mysql.query_db(queries['index'], {})
    '''
    Note: You may not need the `[0]` in the bucket above.
    '''
    # Then, load `Users` page with all Users:
    return render_template('index.html', users_list = users_list)

# Load new User form:
@app.route('/users/new')
def new_user_form():
    # Load `New User` form page:
	return render_template('new_user.html')


# Edit a single User:
@app.route('/users/<id>/edit', methods=["GET"])
def edit_user(id):
    # Query database for User with route paramater `id`:
	user_to_edit = mysql.query_db(queries['show'], {'id': id})[0] # the '[0] will give us a dictionary back instead of a list'
	print user_to_edit
    # Load `Edit User` Page:
	return render_template('edit.html', user_to_edit = user_to_edit)

# Show a Single User or Update User:
@app.route('/users/<id>', methods=["GET", "POST"])
def show_or_update(id):
    '''
    This function either shows the user, or updates the user, depending upon if the
    request method is a `GET` or a `POST`, respectively.
    '''
    # Check if request is `POST` method:
    if request.method == 'POST':
        # Query db with new information to update User:
        mysql.query_db(queries['update'], {
            'id': id, # id from route parameter
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
        })
        return redirect('/users')

    # If request is 'GET', retrieve user with ID
    # Query database for User with route parameter `id`:
    user_to_show = mysql.query_db(queries['show'], {'id': id})[0]
    # Load `View User` Page:
    return render_template('show.html', user = user_to_show)

# Delete a single User:
@app.route('/users/<id>/destroy', methods=["GET"])
def destroy(id):
	flash('User Deleted!')
    # Query database to delete User based on `id`:
	mysql.query_db(queries['delete'], {
        'id': id
    })
    # Redirect to `/users` route (to show all Users):
	return redirect('/users')

#-------------------------#
#----- Run Flask App -----#
#-------------------------#
# Run Flask Application in Debug Mode:
app.run(debug=True)
