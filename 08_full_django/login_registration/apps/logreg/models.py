from __future__ import unicode_literals
import re # import regex library
from django.db import models

class UserManager(models.Manager):
    """
    Extends `Manager` methods to add validation and creation functions.

    Parameters:
    -`models.Manager` - Gives us access to the `Manager` method to which we append additional custom methods.
    """

    def register_validate(self, **kwargs):
        """
        Runs validations on new User.

        Parameters:
        -`self` - Instance to whom this method belongs.
        -`**kwargs` - A dictionary of book data accompanied by two asterisks (mandatory)
        """

        # Create empty errors list to store any errors generated:
        errors = []

        #---------------------#
        #---- VALIDATIONS ----#
        #---------------------#
        """
        + No Existing User
        + First Name - Required; No fewer than 2 characters; letters only
        + Last Name - Required; No fewer than 2 characters; letters only
        + Email - Required; Valid Format
        + Password - Required; No fewer than 8 characters in length; matches Password Confirmation
        """

        #----------------------------#
        #-- FIRST_NAME, LAST_NAME: --#
        #----------------------------#
        # Check if first_name or last_name is less than 2 characters:
        if len(kwargs["first_name"]) < 2 or len(kwargs["last_name"]) < 2:
            print "Error, First and last name are required, and must be at least 2 characters."
            # Add error to list:
            errors.append("First and last name are required must be at least 2 characters.")

        # Check if first_name or last_name contains letters only:
        # Create regex object:
        alphachar_regex = re.compile(r'^[a-zA-Z]*$')
        # Test first_name and last_name against regex object:
        if not alphachar_regex.match(kwargs['first_name']) or not alphachar_regex.match(kwargs['last_name']):
            print "Error, first name and last name must be letters only."
            # Add error to list:
            errors.append("First and last name must be letters only.")

        #------------#
        #-- EMAIL: --#
        #------------#
        # Check if email field is empty:
        if len(kwargs["email"]) < 5:
            print "Email field is required."
            # Add error to list:
            errors.append("Email field is required.")

        # Note: The `else` statements below will only run if the above if statement passes.
        # This is to keep us from giving away too many errors when not quite yet necessary.
        else: # if longer than 5 char:
            # Check if email is in proper format:
            # Create regex object:
            email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            if not email_regex.match(kwargs['email']):
                print "Error, Email format invalid."
                errors.append("Email format is invalid.")
            else: # If passes regex:
                # Check for existing User via email:
                if len(User.objects.filter(email=kwargs["email"])) > 0:
                    print "User with this email address already exists."
                    errors.append("Email address is already registered.")

        #---------------#
        #-- PASSWORD: --#
        #---------------#
        # Check if password is not less than 8 characters:
        if len(kwargs["password"]) < 8:
            print "Error, Password too short."
            # Add error to list:
            errors.append("Password must be at least 8 characters.")
        else:
            # The above else statement is so the code below only runs if the password
            # is more than 8 characters. Again, this is to prevent excessive errors.
            # Check if password matches confirmation password:
            if kwargs["password"] != kwargs["confirm_pwd"]:
                print "Error, Passwords do not match."
                errors.append("Password and confirmation password must match.")

        # Prepare dictionary for Template (saves us some formatting logic in our Controller):
        error_data = {
            "reg_errors": errors
        }

        return error_data

    def login_validate(self, **kwargs):
        """
        Runs validations for User attempting to login.

        Parameters:
        -`self` - Instance to whom this method belongs.
        -`**kwargs` - A dictionary of book data accompanied by two asterisks (mandatory)
        """

        # Create empty errors list to store any errors generated:
        errors = []

        #---------------------#
        #---- VALIDATIONS ----#
        #---------------------#
        """
        + All fields required.
        + Email retrieves existing User.
        + Password matches User's stored password.
        """

        #------------------#
        #---- REQUIRED ----#
        #------------------#
        # Check that all fields are required:
        if len(kwargs["email"]) < 5 or len(kwargs["password"]) < 8:
            print "Error, Email and password are both required."
            # Add error to list:
            errors.append("All fields are required.")

        #------------------#
        #---- EXISTING ----#
        #------------------#
        # Try retrieving existing User:
        try:
            logged_in_user = User.objects.get(email=kwargs["email"])
            print "User has been found..."

            #------------------#
            #---- PASSWORD ----#
            #------------------#
            # Would bcrypt compare password, but for now we'll manually compare fields (WARNING: Unecrypted passwords is a major security risk!)
            # Check if password submitted matches stored password:
            if logged_in_user.password != kwargs["password"]:
                print "Error, Passwords do not match."
                # Add error to error's list:
                errors.append("Login invalid.") # Keep it vauge to give less info to hackers

        except User.DoesNotExist:
            print "Error, User has not been found."
            # Add error to error's list:
            errors.append("Login invalid.")

        # Prepare dictionary for Template (saves us some formatting logic in our Controller):
        error_data = {
            "login_errors": errors
        }

        return error_data

class User(models.Model):
    """
    Creates instances of a `User`.

    Parameters:
    -`models.Model` - Django's `models.Model` method allows us to create new models.
    """

    first_name = models.CharField(max_length=50) # CharField is field type for characters
    last_name = models.CharField(max_length=50) # CharField is field type for characters
    email = models.CharField(max_length=50) # CharField is field type for characters
    password = models.CharField(max_length=22) # CharField is field type for characters
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
    objects = UserManager() # Attaches `UserManager` methods to our `User.objects` object.
