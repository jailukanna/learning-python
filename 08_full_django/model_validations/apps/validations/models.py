# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    """
    Creates custom methods for `User` validation.

    Parameters:
    -`models.Manager` - Extends `.Manager` object to include a new child class and custom methods
    which we can use to validate our `User` object. See: https://docs.djangoproject.com/en/1.11/topics/db/managers/

    See `./views.py` for how we invoke the functions below from our Controller.
    """

    def login(self, **kwargs):
        """
        Accepts any number of arguments and validates login.

        Parameters:
        -`self` - Self is the instance of of `UserManager` class to which these methods are attached.
        -`**kwargs` - Allows for any number of parameters. Warning: Only accepts a dictionary object with two asterisks preceeding it, (ie, `**data`), where `data` is a dictionary. Stands for , "Keyword Arguments".
        """

        print "Login method in `UserManager` now running..."

        print "////// DATA ///////"
        for key, value in kwargs.iteritems():
            print "KEY: {}".format(key)
            print "VALUE: {}".format(value)
            print "///////////////////"

        #-------------------------#
        #------ VALIDATIONS ------#
        #-------------------------#

        # If less than two fields are provided:
        if len(kwargs) < 2:
            print "Number of fields validation failed."
            errors.append("You must provide all fields.")
            return errors

        # If `name` field is less than 2 characters:
        if (len(kwargs["name"]) < 2):
            print "Name validation length failed."
            # Add an error to our previously empty `errors` list:
            errors.append("Your name is too short.")
            # Send back new errors:
            return errors
        else:
            # Login user:
            logged_in_user = User.objects.get(name=kwargs['name'])

            # Print User Info and Send back logged in user:
            print "User has been found and is now logged in."
            print logged_in_user.name, " | ", logged_in_user.email
            return logged_in_user


    def register(self, **kwargs):
        """
        Accepts any number of arguments and validates registration.

        Parameters:
        -`self` - Self is the instance of of `UserManager` class to which these methods are attached.
        -`**kwargs` - Allows for any number of parameters. Warning: Only accepts a dictionary object with two asterisks preceeding it, (ie, `**data`), where `data` is a dictionary. Stands for , "Keyword Arguments".
        """
        # Create Errors list to hold any errors:
        errors = []

        print "Register method in `UserManager` now running..."
        print "////// DATA ///////"
        for key, value in kwargs.iteritems():
            print "KEY: {}".format(key)
            print "VALUE: {}".format(value)
        print "///////////////////"

        #-------------------------#
        #------ VALIDATIONS ------#
        #-------------------------#

        # If less than two fields are provided:
        if len(kwargs) < 2:
            print "Number of fields validation failed."
            errors.append("You must provide all fields.")
            return errors

        # If `name` field is less than 2 characters:
        if (len(kwargs["name"]) < 2):
            print "Name validation length failed."
            # Add an error to our previously empty `errors` list:
            errors.append("Your name is too short.")
            # Send back new errors:
            return errors
        else:
            # Create a new User:
            new_user = User(name=kwargs["name"], email=kwargs["email"])
            # Save the new User (don't forget!):
            new_user.save()
            print new_user
            # Send back new user:
            print "User passed validation and has been created."
            return new_user


class User(models.Model):
    """
    Defines `User` model, which generates instances to be created for DB.

    Parameters:
    -`models.Model` - Tapping into `.Model` allows us to create actual models,
    which will be used to create new tables in whatever DB which is setup.
    """

    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager() # Connects us to our `UserManager` class methods above.
    # Because we've named the above variable, `objects`, we can simply reference
    # `User.objects.{{our_method}}` to invoke it - like `User.objects.login()`.
    # Pretty cool huh?
