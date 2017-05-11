from __future__ import unicode_literals

from django.db import models

# Create your models here.

# this builds our Users table with first_name, last_name, pw_hash, created_at and updated_at columns
# note: you don't have to add a key value
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	pw_hash = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	upated_at = models.DateTimeField(auto_now = True)



# now we'll build our Posts table
class Posts(models.Model):
	title = models.CharField(max_length=45)
	message = models.TextField(max_length=1000)
	user_id = models. ForeignKey(User) # this links a one-to-many relationship to 'User'
 	created_at = models.DateTimeField(auto_now_add = True)
	upated_at = models.DateTimeField(auto_now = True)

# note that any time you make a change to your models, you need to again make your migrations:
	# python manage.py makemigrations
	# python manage.py migrate