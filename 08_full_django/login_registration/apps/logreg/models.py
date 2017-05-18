from __future__ import unicode_literals
import re # import regex library
from django.db import models
from django.contrib import messages # grabs django's `messages` module
from django.contrib.messages import get_messages # lets us access our messages we've created
import bcrypt # grabs `bcrypt` module for encrypting and decrypting passwords

# Add extra message levels to default messaging to handle login or registration error generation:
# https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#creating-custom-message-levels
LOGIN_ERR = 50 # Integer for login errors
REG_ERR = 60 # Integer for registration errors

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
            # Add error to Django's error messaging:
            messages.add_message(kwargs['request'], REG_ERR, 'First and last name are required must be at least 2 characters.', extra_tags="reg_errors")

        # Check if first_name or last_name contains letters only:
        # Create regex object:
        alphachar_regex = re.compile(r'^[a-zA-Z]*$')
        # Test first_name and last_name against regex object:
        if not alphachar_regex.match(kwargs['first_name']) or not alphachar_regex.match(kwargs['last_name']):
            print "Error, first name and last name must be letters only."
            # Add error to Django's error messaging:
            messages.add_message(kwargs['request'], REG_ERR, 'First and last name must be letters only.', extra_tags="reg_errors")

        #------------#
        #-- EMAIL: --#
        #------------#
        # Check if email field is empty:
        if len(kwargs["email"]) < 5:
            print "Email field is required."
            # Add error to Django's error messaging:
            messages.add_message(kwargs['request'], REG_ERR, 'Email field is required.', extra_tags="reg_errors")

        # Note: The `else` statements below will only run if the above if statement passes.
        # This is to keep us from giving away too many errors when not quite yet necessary.
        else: # if longer than 5 char:
            # Check if email is in proper format:
            # Create regex object:
            email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            if not email_regex.match(kwargs['email']):
                print "Error, Email format invalid."
                # Add error to Django's error messaging:
                messages.add_message(kwargs['request'], REG_ERR, 'Email format is invalid.', extra_tags="reg_errors")
            else: # If passes regex:
                # Check for existing User via email:
                if len(User.objects.filter(email=kwargs["email"])) > 0:
                    print "User with this email address already exists."
                    # Add error to Django's error messaging:
                    messages.add_message(kwargs['request'], REG_ERR, 'Email address already registered.', extra_tags="reg_errors")

        #---------------#
        #-- PASSWORD: --#
        #---------------#
        # Check if password is not less than 8 characters:
        if len(kwargs["password"]) < 8:
            print "Error, Password too short."
            # Add error to Django's error messaging:
            messages.add_message(kwargs['request'], REG_ERR, 'Password fields are required and must be at least 8 characters.', extra_tags="reg_errors")
        # Otherwise check if it matches the confirmation. If it does, bcrpyt it and send it back.
        else:
            # The above else statement is so the code below only runs if the password
            # is more than 8 characters. Again, this is to prevent excessive errors.
            # Check if password matches confirmation password:
            if kwargs["password"] != kwargs["confirm_pwd"]:
                print "Error, Passwords do not match."
                # Add error to Django's error messaging:
                messages.add_message(kwargs['request'], REG_ERR, 'Password and confirmation password must match.', extra_tags="reg_errors")

        # If no validation errors, hash password and send back validated data:
        # Get current errors:
        errors = get_messages(kwargs["request"])
        if len(errors) == 0:
            # Hash Password:
            kwargs["password"] = bcrypt.hashpw(kwargs["password"].encode(), bcrypt.gensalt(14))
            # Delete request object we used for Django messaging:
            if kwargs.has_key("request"):
                kwargs.pop("request")
            # Send Validated User Data (now with Hashed Password) for Instance Creation:
            return kwargs
        # If validation errors, send back None:
        else:
            print "Errors validating User registration."
            for error in errors:
                print "Validation Error: ", error
            return None

    def login_validate(self, **kwargs):
        """
        Runs validations for User attempting to login.

        Parameters:
        -`self` - Instance to whom this method belongs.
        -`**kwargs` - A dictionary of book data accompanied by two asterisks (mandatory)
        """

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
            # Add error to Django's error messaging:
            messages.add_message(kwargs['request'], LOGIN_ERR, 'All fields are required.', extra_tags="login_errors")
        # If all fields are filled in:
        else:
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
                # Compare passwords with bcrypt:
                # Notes: We pass in our `kwargs['password']` chained to the `str.encode()` method so it's ready for bcrypt.
                # We could break this down into a separate variable, but instead we do it all at once for zen simplicity's sake.
                # The zen master answers, "I have no sake."
                if bcrypt.hashpw(kwargs["password"].encode(), logged_in_user.password.encode()) != logged_in_user.password:
                    print("Error, Password is incorrect.")
                    # Add error to Django's error messaging:
                    messages.add_message(kwargs['request'], LOGIN_ERR, 'Login invalid.', extra_tags="login_errors")

            except User.DoesNotExist:
                print "Error, User has not been found."
                # Add error to Django's error messaging:
                messages.add_message(kwargs['request'], LOGIN_ERR, 'Login invalid.', extra_tags="login_errors")

        # If no validation errors, send back True:
        # Get current errors:
        errors = get_messages(kwargs["request"])
        if len(errors) == 0:
            # Delete request object we used for Django messaging:
            if kwargs.has_key("request"):
                kwargs.pop("request")
            # Send True indicating Validation has been passed:
            return True
        # If validation errors, send back None:
        else:
            print "Errors validating User login."
            for error in errors:
                print "Validation Error: ", error
            return None

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
