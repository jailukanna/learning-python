'''
# Part 1: Table Creation via SQLite / aka Models in the "MVC" / "MTV" Structure:

Note: Django can be setup to use various database backends. By default, SQLite
is setup, and that is what these notes apply to. According to the documentation,
if you did setup a different database, the same model methods would apply, and be
automatically converted to your DB of choice (but I've never tried anything other
than SQLite with Django so far).

Here's more info:
https://docs.djangoproject.com/en/1.11/topics/db/models/

In the meantime, let's go ahead and learn to setup some models.

We'll have to do two things:
1. Import the django models module
2. Create a class with the proper syntax (will be our model)
'''

# Inside models.py
from __future__ import unicode_literals
# imports Django's models module (say that three times fast):
from django.db import models

# Our Super Basic Model.
# Note: When we create our model properties, we have to define a "column type".
# Checkout the different column types below the class definition for more information.

class People(models.Model):
	first_name = models.CharField(max_length=30) # CharField is a "column type"
	last_name = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is a "column type"
 	updated_at = models.DateTimeField(auto_now=True)

'''
Column Types:

	AutoField
	Don’t worry about this field too much; it’s created for us automatically

	CharField
	Any text that can be small to large that a user may enter

	DateField
	Used for dates. Can have optional parameters such as auto_now_add=True which adds the current date when object is created

	DateTimeField
	Same concept as DateField, but has added optional parameters

'''

# NOTE: After you've built a database, you have to forward engineer it!

'''
To forward engineer the database above, we have to makemigration:

In Terminal (BASH):

  timotree$ python manage.py makemigrations
  timotree$ python manage.py migrate

Remember:

Never delete migration files, and always makemigrations
and migrate anytime you change something in your
models.py files – that’s what updates the actual
database so it reflects what’s in your models.


The first command (makemigrations) tells Django:

“Look and see if there have been any changes to the models
files in our apps. If so, create the code (using built-in
Django methods) that represents those changes.”


The second command (migrate) says:

Forward engineer those changes into our database! (I.e.
turn the code generated inside a migration file into SQL
commands and run those commands in local memory)


For development, we are going to be using SQLite - a
prepackaged SQL database that has much of the functionality
of MySQL (but not all of it) and is stored as local memory.

For deployment we are going to be using postGRES, a SQL
database that has some added functionality, making it a bit
heavier, but a solid deployment option.

We may also deploy with a MySQL database, which is a little bit faster than
postGRES).
'''

'''
# Part 2: Querying DB using Django commands:

# In `views.py`:

from django.shortcuts import render
from .models import People #load models.py for people class

def index(request):
    People.objects.create(first_name=“Mike”,last_name=“Hannon”) # creates item in table
    people = People.objects.all() # gets all objects in `People` table
    print people # prints this list
    return render(request,”third_app/index.html”)
'''






'''
MANY TO ONE RELATIONSHIP EXAMPLE

'One user can have many posts'

Users -< Posts

'''

 # Inside models.py
  from __future__ import unicode_literals
  from django.db import models
  # Create your models here.

  # this is our 'users table'
  class User(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

  # this is our posts table
  # because we've included a linkage to models.ForeignKey(User), this is also a one to many relationship: one user can have many posts
  class Post(models.Model):
      title = models.CharField(max_length=45)
      message = models.TextField(max_length=1000)
      # Notice the association made with ForeignKey for a one-to-many relationship
      user_id = models.ForeignKey(User)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
