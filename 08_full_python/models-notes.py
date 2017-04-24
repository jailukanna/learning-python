 '''
 SINGLE TABLE CREATION VIA SQLIGHT
 '''



# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Our Super Basic Model.
class People(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
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



'''

to forward engineer the database above, we'd have to makemigrations:

  > python manage.py makemigrations
  > python manage.py migrate

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
heavier, but a solid deployment option. (Alternatively, with 
some fiddling you can also deploy a MySQL database, which is 
a little bit faster than postGRES).

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
