from __future__ import unicode_literals
import re # import regex library
from django.db import models
from django.contrib import messages # grabs django's `messages` module
from django.contrib.messages import get_messages # lets us access our messages we've created
import bcrypt # grabs `bcrypt` module for encrypting and decrypting passwords

# Add extra message levels to default messaging to handle login or registration error generation:
# https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#creating-custom-message-levels
LOGIN_ERR = 50 # Messages level for login errors
REG_ERR = 60 # Messages level for registration errors

class UserManager(models.Manager):
    """
    Extends `Manager` methods to add validation and creation functions.

    Parameters:
    - `models.Manager` - Gives us access to the `Manager` method to which we
    append additional custom methods.

    Functions:
    - `register_validate(self, **kwargs)` - Accepts a dictionary list of
    registration form arguments. Either returns False if validation fails, or
    returns the validated and newly created `User`.
    - `login_validate(self, **kwargs)` - Accepts a dictionary list of login
    form arguments. Either returns False if validation fails, or returns the
    validated retrieved user.

    Notes:
    All validations, password hashing and creation or retrieval of objects from
    the DB occurs in this file.
    """

    def register_validate(self, request):
        """
        Runs validations on new User.

        Parameters:
        - `self` - Instance to whom this method belongs.
        - `request` - The full request object: includes form data and the request object itself for django-messages

        Validations:
        - First Name - Required; No fewer than 2 characters; letters only
        - Last Name - Required; No fewer than 2 characters; letters only
        - Email - Required; Valid Format
        - No Existing User - Check by email
        - Password - Required; No fewer than 8 characters in length; matches Password Confirmation
        """

        #---------------------------#
        #-- FIRST_NAME/LAST_NAME: --#
        #---------------------------#
        # Check if first_name or last_name is less than 2 characters:
        if len(request.POST["first_name"]) < 2 or len(request.POST["last_name"]) < 2:
            # Add error to Django's error messaging:
            messages.add_message(request, REG_ERR, 'First and last name are required must be at least 2 characters.', extra_tags="reg_errors")

        # Check if first_name or last_name contains letters only:
        alphachar_regex = re.compile(r'^[a-zA-Z]*$') # Create regex object
        # Test first_name and last_name against regex object:
        if not alphachar_regex.match(request.POST["first_name"]) or not alphachar_regex.match(request.POST["last_name"]):
            # Add error to Django's error messaging:
            messages.add_message(request, REG_ERR, 'First and last name must be letters only.', extra_tags="reg_errors")

        #------------#
        #-- EMAIL: --#
        #------------#
        # Check if email field is empty:
        if len(request.POST["email"]) < 5:
            messages.add_message(request, REG_ERR, 'Email field is required.', extra_tags="reg_errors")

        # Note: The `else` statements below will only run if the above if statement passes.
        # This is to keep us from giving away too many errors when not quite yet necessary.
        else: # if longer than 5 char:
            # Check if email is in proper format:
            # Create regex object:
            email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            if not email_regex.match(request.POST["email"]):
                messages.add_message(request, REG_ERR, 'Email format is invalid.', extra_tags="reg_errors")
            else: # If passes regex:
                #---------------#
                #-- EXISTING: --#
                #---------------#
                # Check for existing User via email:
                if len(User.objects.filter(email=request.POST["email"])) > 0:
                    messages.add_message(request, REG_ERR, 'Email address already registered.', extra_tags="reg_errors")

        #---------------#
        #-- PASSWORD: --#
        #---------------#
        # Check if password is not less than 8 characters:
        if len(request.POST["password"]) < 8:
            # Add error to Django's error messaging:
            messages.add_message(request, REG_ERR, 'Password fields are required and must be at least 8 characters.', extra_tags="reg_errors")
        # Otherwise check if it matches the confirmation. If it does, bcrpyt it and send it back.
        else:
            # The above else statement is so the code below only runs if the password
            # is more than 8 characters. Again, this is to prevent excessive errors.
            # Check if password matches confirmation password:
            if request.POST["password"] != request.POST["confirm_pwd"]:
                messages.add_message(request, REG_ERR, 'Password and confirmation password must match.', extra_tags="reg_errors")

        # Get current errors to check if any exist:
        errors = get_messages(request)

        # If no validation errors, hash password, create user and send new user back:
        if len(errors) == 0:
            print "Registration data passed validation..."
            print "Hashing password..."
            # Hash Password:
            hashed_pwd = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt(14))
            print "Password hashed."
            print "Creating new user with data..."
            # Create new validated User:
            # Note: Be sure to use `hashed_pwd`, not the original password.
            validated_user = {
                "logged_in_user": User(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=hashed_pwd)
            }
            # Save new User:
            validated_user["logged_in_user"].save()
            print "New `User` created:"
            print "{} {} | {} | {}".format(validated_user["logged_in_user"].first_name,validated_user["logged_in_user"].last_name, validated_user["logged_in_user"].email, validated_user["logged_in_user"].created_at)
            print "Logging user in..." # // Development Improvement Note: // Could assign Session here.
            # Send newly created validated User back:
            return validated_user
        # Else, if validation fails print errors to console and return `False`:
        else:
            print "Errors validating User registration."
            for error in errors:
                print "Validation Error: ", error
            return False

    def login_validate(self, request):
        """
        Runs validations for User attempting to login.

        Parameters:
        - `self` - Instance to whom this method belongs.
        - `request` - The full request object: includes form data and the request object itself for django-messages

        Validations:
        - All fields required.
        - Email retrieves existing User.
        - Password matches User's stored password (bcrypted).
        """

        #------------------#
        #--- ALL FIELDS ---#
        #------------------#
        # Check that all fields are required:
        # Note: the fields for our login form, are `login_email` and `login_password`, instead of simply `email` or `password` as used above.
        if len(request.POST["login_email"]) < 5 or len(request.POST["login_password"]) < 8:
            # Add error to Django's error messaging:
            messages.add_message(request, LOGIN_ERR, 'All fields are required.', extra_tags="login_errors")
        # If all fields are filled in:
        else:
            #------------------#
            #---- EXISTING ----#
            #------------------#
            # Try retrieving existing User:
            try:
                logged_in_user = User.objects.get(email=request.POST["login_email"])
                print "User has been found..."

                #------------------#
                #---- PASSWORD ----#
                #------------------#
                # Compare passwords with bcrypt:
                # Notes: We pass in our `kwargs['password']` chained to the `str.encode()` method so it's ready for bcrypt.
                # We could break this down into a separate variable, but instead we do it all at once for zen simplicity's sake.
                # The zen master answers, "I have no sake."
                if bcrypt.hashpw(request.POST["login_password"].encode(), logged_in_user.password.encode()) != logged_in_user.password:
                    print("Error, Password is incorrect.")
                    messages.add_message(request, LOGIN_ERR, 'Login invalid.', extra_tags="login_errors")

            except User.DoesNotExist:
                print "Error, User has not been found."
                messages.add_message(request, LOGIN_ERR, 'Login invalid.', extra_tags="login_errors")

        # Get current errors to check if any exist:
        errors = get_messages(request)

        # If no validation errors, send back True:
        if len(errors) == 0:
            print "Login data passed validation..."
            print "Logging user in..." # // Development Improvement Note: // Could assign Session here.
            # Send back validated retrieved user:
            validated_user = {
                "logged_in_user": logged_in_user, # email of our retrieved `User` from above validations.
            }
            return validated_user
        # Else, if validation fails print errors to console and return `False`:
        else:
            print "Errors validating User login."
            for error in errors:
                print "Validation Error: ", error
            return False

class User(models.Model):
    """
    Creates instances of a `User`.

    Parameters:
    -`models.Model` - Django's `models.Model` method allows us to create new models.
    """

    first_name = models.CharField(max_length=50) # CharField is field type for characters
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=22)
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
    objects = UserManager() # Attaches `UserManager` methods to our `User.objects` object.
