from __future__ import unicode_literals

from django.db import models
import re # regex
import bcrypt # grabs `bcrypt` module for encrypting and decrypting passwords

class UserManager(models.Manager):
    """
    Extends `Manager` methods to add validation and creation functions.

    Parameters:
    - `models.Manager` - Gives us access to the `Manager` method to which we
    append additional custom methods.

    Functions:
    - `register_validate(self, **kwargs)` - Accepts a dictionary list of
    registration form arguments. Either returns errors list if validation fails, or
    hashes password and returns the validated and newly created `User`.
    - `login_validate(self, **kwargs)` - Accepts a dictionary list of login
    form arguments. Either returns errors list if validation fails, or returns the
    validated retrieved user.
    """

    def register_validate(self, **kwargs):
        """
        Runs validations on new User.

        Parameters:
        - `self` - Instance to whom this method belongs.
        - `**kwargs` - Dictionary object of registration values from controller to be validated.

        Validations:
        - First Name - Required; No fewer than 2 characters; letters only
        - Last Name - Required; No fewer than 2 characters; letters only
        - Email - Required; Valid Format
        - No Existing User - Check by email
        - Password - Required; No fewer than 8 characters in length; matches Password Confirmation
        """

        # Create empty errors list, which we'll return to generate django messages back in views.py:
        errors = []

        #---------------------------#
        #-- FIRST_NAME/LAST_NAME: --#
        #---------------------------#
        # Check if first_name or last_name is less than 2 characters:
        if len(kwargs["first_name"]) < 2 or len(kwargs["last_name"]) < 2:
            # Add error to error's list:
            errors.append('First and last name are required must be at least 2 characters.')

        # Check if first_name or last_name contains letters only:
        alphachar_regex = re.compile(r'^[a-zA-Z]*$') # Create regex object
        # Test first_name and last_name against regex object:
        if not alphachar_regex.match(kwargs["first_name"]) or not alphachar_regex.match(kwargs["last_name"]):
            # Add error to error's list:
            errors.append('First and last name must be letters only.')

        #------------#
        #-- EMAIL: --#
        #------------#
        # Check if email field is empty:
        if len(kwargs["email"]) < 5:
            # Add error to error's list:
            errors.append('Email field is required.')

        # Note: The `else` statements below will only run if the above if statement passes.
        # This is to keep us from giving away too many errors when not quite yet necessary.
        else: # if longer than 5 char:
            # Check if email is in proper format:
            # Create regex object:
            email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
            if not email_regex.match(kwargs["email"]):
                # Add error to error's list:
                errors.append('Email format is invalid.')
            else: # If passes regex:
                #---------------#
                #-- EXISTING: --#
                #---------------#
                # Check for existing User via email:
                if len(User.objects.filter(email=kwargs["email"])) > 0:
                    # Add error to error's list:
                    errors.append('Email address already registered.')

        #---------------#
        #-- PASSWORD: --#
        #---------------#
        # Check if password is not less than 8 characters:
        if len(kwargs["password"]) < 8:
            # Add error to error's list:
            errors.append('Password fields are required and must be at least 8 characters.')
        # Otherwise check if it matches the confirmation. If it does, bcrpyt it and send it back.
        else:
            # The above else statement is so the code below only runs if the password
            # is more than 8 characters. Again, this is to prevent excessive errors.
            # Check if password matches confirmation password:
            if kwargs["password"] != kwargs["confirm_pwd"]:
                # Add error to error's list:
                errors.append('Password and confirmation password must match.')

        # If no validation errors, hash password, create user and send new user back:
        if len(errors) == 0:
            print "Registration data passed validation..."
            print "Hashing password..."
            # Hash Password:
            kwargs["password"] = bcrypt.hashpw(kwargs["password"].encode(), bcrypt.gensalt(14))
            print "Password hashed."
            print "Creating new user with data..."
            # Create new validated User:
            validated_user = {
                "logged_in_user": User(first_name=kwargs["first_name"], last_name=kwargs["last_name"], email=kwargs["email"], password=kwargs["password"])
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
            # Prepare data for `views.py`:
            errors = {
                "errors": errors,
            }
            return errors

    def login_validate(self, **kwargs):
        """
        Runs validations for User attempting to login.

        Parameters:
        - `self` - Instance to whom this method belongs.
        - `**kwargs` - Dictionary object of login values from controller to be validated.

        Validations:
        - All fields required.
        - Email retrieves existing User.
        - Password matches User's stored password (bcrypted).
        """

        # Create empty errors list, which we'll return to generate django messages back in views.py:
        errors = []

        #------------------#
        #--- ALL FIELDS ---#
        #------------------#
        # Check that all fields are required:
        if len(kwargs["email"]) < 5 or len(kwargs["password"]) < 8:
            # Add error to error's list:
            errors.append('All fields are required.')
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
                    # Add error to error's list:
                    errors.append('Login invalid.')

            except User.DoesNotExist:
                print "Error, User has not been found."
                # Add error to error's list:
                errors.append('Login invalid.')

        # If no validation errors, send back True:
        if len(errors) == 0:
            print "Login data passed validation..."
            print "Logging user in..." # // Development Improvement Note: // Could assign Session here.
            # Prepare data for Template:
            validated_user = {
                "logged_in_user": logged_in_user, # email of our retrieved `User` from above validations.
            }
            # Send back retrieved User:
            return validated_user
        # Else, if validation fails print errors to console and return `False`:
        else:
            print "Errors validating User login."
            for error in errors:
                print "Validation Error: ", error
            # Prepare data for `views.py`:
            errors = {
                "errors": errors,
            }
            return errors

class SecretManager(models.Manager):
    """
    Extends `Manager` methods to add validation and creation functions.

    Parameters:
    - `models.Manager` - Gives us access to the `Manager` method to which we
    append additional custom methods.

    Functions:
    - `secret_validate(self, **kwargs)` - Accepts a dictionary list of
    secret form arguments. Either returns errors list if validation fails, or
    returns the validated and newly created `Secret`.
    """

    def secret_validate(self, **kwargs):
        """
        Runs validations on new Secret.

        Parameters:
        - `self` - Instance to whom this method belongs.
        - `*kwargs` - Dictionary of secret data to be validated.

        Validations:
        - Desription - Required; No fewer than 5 characters.
        """

        # Create empty errors list, which we'll return to generate django messages back in views.py:
        errors = []

        #------------------#
        #-- DESCRIPTION: --#
        #------------------#
        # Check if description is less than 5 characters:
        if len(kwargs["description"]) < 5:
            # Add error to error's list:
            errors.append('Secret must be at least 5 characters.')


        # If no validation errors, create new Secret:
        if len(errors) == 0:
            print "Secret description passed validation..."
            # Retrieve current User by ID:
            print "Retrieving current user..."
            user = User.objects.get(id=kwargs["user_id"])
            print "Creating new secret with data..."
            # Create new validated Secret:
            validated_secret = {
                "secret": Secret(description=kwargs["description"], user=user),
                "logged_in_user": User.objects.get(id=kwargs["user_id"]), # you might be able to remove this and streamline it with a helper function
            }
            # Save new Secret:
            validated_secret["secret"].save()
            print "New `Secret` created:"
            print "'{}' - {} {} - {}".format(validated_secret["secret"].description, validated_secret["secret"].user.first_name, validated_secret["secret"].user.first_name, validated_secret["secret"].created_at)
            # Send newly created validated Secret back:
            return validated_secret
        # Else, if validation fails print errors to console and return errors list:
        else:
            print "Errors validating Secret."
            for error in errors:
                print "Validation Error: ", error
            # Prepare data for `views.py`:
            errors = {
                "errors": errors,
            }
            return errors

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

class Secret(models.Model):
    """
    Creates instances of a `Secret`.

    Parameters:
    -`models.Model` - Django's `models.Model` method allows us to create new models.
    """

    description = models.CharField(max_length=100) # CharField is field type for characters
    user = models.ForeignKey(User, related_name="secrets") # One-to-Many Relationship
    likes = models.ManyToManyField(User, related_name="liked") # Many to Many Relationship
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
    objects = SecretManager() # Attaches `SecretManager` methods to our `Secret.objects` object.
