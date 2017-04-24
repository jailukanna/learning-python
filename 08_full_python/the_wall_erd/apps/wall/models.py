from __future__ import unicode_literals

from django.db import models
'''
Note: this assignment is to recreate the wall erd using django:
3 tables:
	+ Users table 
		+ first_name 
		+ last_name
		+ pw_hash
		+ email
		+ created_at
		+ updated_at

	+ Messages table
		+ user_id = models.ForeignKey (many messages for one user)
		+ message
		+ created_at
		+ updated_at

	+ Comments table
		+ message_id = models.ForeignKey (many comments for one message)
		+ user_id = models.ForeignKey (many comments for one user)
		+ comment
		+ created_at
		+ updated_at
'''
# Create your models here.

class Users(models.Model): # note normally we title our tables Uppercase and singular
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	pw_hash = models.CharField(max_length=100)
	email = models.EmailField(max_length=200)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Messages(models.Model):
	user_id = models.ForeignKey(Users) # most often, this would be titled 'user' instead of 'user_id' but is kept that way as you build familarity
	message = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Comments(models.Model):
	message_id = models.ForeignKey(Messages)
	user_id = models.ForeignKey(Users)
	comment = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)