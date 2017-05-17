from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    """
    Extends `Manager` methods to add validation and creation functions.

    Parameters:
    -`models.Manager` - Gives us access to the `Manager` method to which we append additional custom methods.
    """

    def validate(self, **kwargs):
        """
        Runs validations on new User.

        Parameters:
        -`self` - Instance to whom this method belongs.
        -`**kwargs` - A dictionary of book data accompanied by two asterisks (mandatory)
        """

        # Create empty errors list to store any errors generated:
        errors = []

        # Check if username is less than 8 characters:
        if len(kwargs["username"]) < 8:
            print "Username must be more than 8 characters."
            # Add error to list:
            errors.append("Username must be at least 8 characters.")

        # Check if username is more than 16 characters:
        if len(kwargs["username"]) > 16:
            print "Username must be less than 16 characters."
            # Add error to list:
            errors.append("Username must less than 16 characters.")

        return errors

class User(models.Model):
    """
    Creates instances of a `User`.

    Parameters:
    -`models.Model` - Django's `models.Model` method allows us to create new models.
    """

    username = models.CharField(max_length=50) # CharField is field type for characters
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
    objects = UserManager() # Attaches `UserManager` methods to our `User.objects` object.
