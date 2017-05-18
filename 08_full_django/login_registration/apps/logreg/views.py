# Import dependencies:
from django.shortcuts import render, redirect # Render templates and redirect routes.
from models import User # Gives us access to `User` model
import bcrypt # grabs bcrypt module for encrypting and decrypting passwords

def index(request):
    """Loads index page which is a login/registration page."""

    # If request method is a "POST", begin process of validating credentials logging user in:
    if request.method == "POST":
        # Prepare data as dict for validation:
        login_data = {
            "request": request, # The `request` object is required when using Django messaging, which we use for validations in our `models.py` `login_validate()` method.
            "email": request.POST["login_email"],
            "password": request.POST["login_password"] # would normally bcrypt password here
        }
        """
        Note for improvement: I don't know if it's bad to pass the entire request
        object along like I did in the dictionary above. The only reason I did this,
        was because in order to use Django's `messaging` module, one of the required
        arguments was the `request` object, since this is what the module attaches
        the messages to. *If* it was bad to do this for performance or memory reasons,
        another strategy might be to bypass the module, and create a list of errors,
        to which, once handed back to `views.py` (of where the `request` object is available),
        could then be plugged into django messages (using a for loop).
        """
        # Validate credentials submitted to login form:
        validated = User.objects.login_validate(**login_data)
        # If errors, load homepage with errors:
        if validated == False:
            print "Errors logging in user."
            return render(request, "logreg/index.html") # you must render, not rediret, so `request` object gets updated with django messages
        # If credentials are validated, load success page along with `logged_in_user`:
        else:
            # Prepare logged_in_user data for Template:
            """
            Note for Improvement: Might want to use a Try/Except statement to handle
            the User.get() method below, in case that no user was retrieved. Remember,
            we of course did validate for this previously, so it theoretically should NEVER EVER
            come back empty, but hey, you never know....I guess it might be good to close open
            doors in case others try and exploit the code's intention.
            """
            logged_in_user = {
                "logged_in_user": User.objects.get(email=login_data["email"])
            }
            # Load success page along with logged in user data:
            return render(request, "logreg/success.html", logged_in_user)

    # If request method is "GET", load homepage:
    return render(request, "logreg/index.html")

def register(request):
    """Validates, and if successful, creates a new `User`."""

    # If request method is "POST", begin validate form then create user if validation successful:
    if request.method == "POST":
        print "Validating registration form..."
        # Prepare form data as dict for validation:
        register_data = {
            "request": request, # this is to give django messages access to request...not sure if this loses performance but had to pass this object to access messages in models
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "confirm_pwd": request.POST["confirm_pwd"],
        }
        # Validate registration data submitted from registration form:
        """
        Note: Double asterisks `**` must be included along with dict obj below for
        the `register_validate(**kwargs)` function to work. This function either
        returns `False` if validation fails, or returns validated user data with
        the password now encrypted and ready for creation.
        """
        validated = User.objects.register_validate(**register_data) # see `./models.py`, `register_validate()`
        # If errors, reload index page (Django will load error objects):
        if validated == False:
            print "Errors validating user registration..."
            print validated
            # Return to index with updated request object (which contains our error messages):
            # Note: If we did a `redirect` to our index route, our django message data would not display,
            # as it is stored in the updated request object.
            return render(request, "logreg/index.html")
        # If validation successful, create new user and send it along with success page:
        else:
            print "Registration data passed validation..."
            print "Creating new user with validated data...."
            # Create new user (as dict object) to make it ready for Template:
            """
            IMPORTANT: Be sure that the password is the validated password
            (bcrypted) when creating your new User in the dictionary below. This
            lives in the `validated` object above, as `validated["password"]`.
            Do NOT use the password in the `registered_data` dictionary, as this
            is not encrypted, and an unencrypted password would be stored in the
            database.
            """
            logged_in_user = {
                "logged_in_user": User(first_name=register_data['first_name'], last_name=register_data['last_name'], email=register_data['email'], password=validated['password']),
            }
            # Save new `User`:
            logged_in_user["logged_in_user"].save()
            # Load success page with `logged_in_user` dictionary
            return render(request, "logreg/success.html", logged_in_user)

    # If request route on `/register` is "GET", redirect to index (not a function in our application but security for our route):
    elif request.method == "GET":
        # Redirect to homepage:
        return redirect('/')
