# Model Validations:

This project allows us to tap into `models.Manager` and add our own child classes.
In these child classes, we can create methods which we use to validate:

Now that we can insert data, it's time to validate the user's input before inserting those values into the database. The code we're going to use for validating data will look familiar, just like we did in Flask. However, we're going to set up our code to be a part of our models, since models should be doing everything database-related.

Let's start off by adding our validation to the User model:

First, let's make a User model.

  # Inside your app's models.py file
  from __future__ import unicode_literals
  from django.db import models
  # Create your models here.
  class User(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
"""
models come with a hidden key:
      objects = models.Manager()
we are going to overwrite this!
"""

Models inheriting from the model class include a property, objects, something we've touched on already and you've used when running query methods. This objects includes all those ORM query methods that are so convenient, like .all(), .get(), etc. We can extend this functionality using the Manager class. Let's look at how to do so.

To do this, we are going to make a new property for our User class and have that property be a reference to our manager. This Manager class is another built-in Django class used to extend our models' functionality.

Let's create a new class UserManager and add it to our previous code.

Important: Notice that our User and UserManager classes are inheriting from entirely different models.
By inheriting from models.Model, User is made into a database table. models.Manager, however, means our UserManager will inherit from the ORM-building class.
  # Inside your app's models.py file
  from __future__ import unicode_literals
  from django.db import models
  #Our new manager!
  #No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
  class UserManager(models.Manager):
      def login(self, postData):
          print "Running a login function!"
          print "If successful login occurs, maybe return {'theuser':user} where user is a user object?")
          print "If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }"
      def register(self, postData):
          print ("Register a user here")
          print ("If successful, maybe return {'theuser':user} where user is a user object?")
          print ("If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short'] ")
  class User(models.Model):
      first_name = models.CharField(max_length=45)
      last_name = models.CharField(max_length=45)
      password = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # *************************
      # Connect an instance of UserManager to our User model overwriting
      # the old hidden objects key with a new one with extra properties!!!
      objects = UserManager()
      # *************************

Now in our views.py file, we can use User.objects.login(data) and .register(data):

  # Inside your app's views.py file
  from django.shortcuts import render, HttpResponse, redirect
  from .models import User
  def index(request):
      print("Running index method, calling out to User.")
      user = User.objects.login("speros@codingdojo.com","Speros")
# DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
      print (type(user))
      if 'error' in user:
          pass
      if 'theuser' in user:
          pass
      return HttpResponse("Done running userManager method. Check your terminal console.")

Feel free to experiment with the UserManager methods – any change you make to that class does not need to be migrated since it's not a database table. (Note in the video I use userManager, rather than objects to call the userManager specific methods for clarity).
