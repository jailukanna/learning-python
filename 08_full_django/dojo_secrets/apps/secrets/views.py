from django.shortcuts import render, redirect
from models import User, Secret # Gives us access to `User` and `Secret` models
from django.contrib import messages # grabs django's `messages` module
from django.forms.models import model_to_dict # Let's us jsonify django model data for use in sessions

# Add extra message levels to default messaging to handle login or registration error generation:
# https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#creating-custom-message-levels
LOGIN_ERR = 50 # Messages level for login errors
REG_ERR = 60 # Messages level for registration errors
SECRET_ERR = 70 # Messages level for secret errors

def index(request):
    """
    Loads login/registration homepage.

    Notes: If request method is a POST, user registration will run (with validation)
    and user will be redirected to the dashboard. If request method is a GET,
    login and registration page will load instead.
    """

    # If request method is a POST, validate and register:
    if request.method == "POST":
        # Prepare registration data for validation:
        reg_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "confirm_pwd": request.POST["confirm_pwd"],
        }
        # Validate registration data:
        validated = User.objects.register_validate(**reg_data) # see `./models.py`, `register_validate()`
        # If errors, reload index page (Django will load error objects):
        try:
            if len(validated["errors"]) > 0:
                print "User could not be registered."
                # Generate Django errors:
                for error in validated["errors"]:
                    # Add error to Django's error messaging:
                    messages.add_message(request, REG_ERR, error, extra_tags="reg_errors")
                # Send back index with updated request object (which contains our Django error messages):
                # Note: If we did a `redirect` to our index route, our django message data would not display,
                # as it is stored in the updated request object.
                return render(request, "secrets/index.html")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                return redirect('/')
        # If validation successful, create new user and send it along with success page:
        except KeyError:
            # Set session to validated User:
            request.session["user_id"] = validated["logged_in_user"].id
            # Load dashboard page with `validated` user (already returned as a `dict` obj.)
            return render(request, "secrets/dashboard.html", validated)
    # If request method is not POST, load login/registration page:
    else:
        return render(request, "secrets/index.html")

def login(request):
    """
    Logs in and validates current user.

    Notes: If successful, retrieve validated user and load dashboard page. Otherwise,
    reload index page with django errors.
    """
    # If request method is a POST, validate and login:
    if request.method == "POST":
        print "Logging in User..."
        # Prepare user submitted data for validation:
        login_data = {
            "email": request.POST["login_email"],
            "password": request.POST["login_password"],
        }
        validated = User.objects.login_validate(**login_data) # pass entire request object as we need this for creating django-messages
        try:
            # If errors, load homepage with errors:
            if len(validated["errors"]) > 0:
                print "User could not be logged in."
                # Generate Django errors:
                for error in validated["errors"]:
                    # Add error to Django's error messaging:
                    messages.add_message(request, LOGIN_ERR, error, extra_tags="login_errors")
                # We must render, not redirect, so `request` object gets updated with django messages:
                # If we redirect, the request object is updated and our old modified one with the messages is lost.
                return render(request, "secrets/index.html")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                return redirect('/') # Added for extra security to cover all cases.
        # If credentials are validated, load success page along with `logged_in_user`:
        except KeyError:
            # Set session to validated User:
            request.session["user_id"] = validated["logged_in_user"].id
            # Return dashboard page with the validated user.
            return render(request, "secrets/dashboard.html", validated)
    # If request method is not a POST, reload index as this is an unexpected request:
    else:
        print "Unexpected errors occurred."
        messages.add_message(request, LOGIN_ERR, "An unexpected error has occurred.", extra_tags="login_errors")
        return redirect("/")

def new_secret(request):
    """Creates new secrets."""

    # If request method POST, validate and create new secret.
    if request.method == "POST":
        # Prepare data for validation:
        secret_data = {
            "description": request.POST["description"],
            "user_id": request.session["user_id"], # Retrieves session stored ID
        }
        # Validate seceret:
        validated = Secret.objects.secret_validate(**secret_data)
        try:
            # If errors, load dashboard with errors:
            if len(validated["errors"]) > 0:
                print "Secret could not be validated."
                # Generate Django errors:
                for error in validated["errors"]:
                    # Add error to Django's error messaging:
                    messages.add_message(request, SECRET_ERR, error, extra_tags="secret_errors")
                # We must render, not redirect, so `request` object gets updated with django messages:
                # If we redirect, the request object is updated and our old modified one with the messages is lost.
                return render(request, "secrets/dashboard.html")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                return redirect('/') # Added for extra security to cover all cases.
        # If secret is validated, get recent secrets/popular secrets and load dashboard:
        except KeyError:
            # Get recent secrets:
            # Get popular secrets:
            # Get count of likes:
            # Format data for template:
            return render(request, "secrets/dashboard.html", validated)

    # If request method is not POST, return to dashboard as this is an unexpected request:
    else:
        print "Unexpected errors occurred."
        messages.add_message(request, SECRET_ERR, "An unexpected error has occurred.", extra_tags="secret_errors")
        return render(request, "secrets/dashboard.html")


"""
DO THIS:

-- Build 1 function which receives new secret, validates, and then loads dashboard.
-- Build 1 function which does the functions below (grabs recent secrets, grabs most popular secrets).
-- Create a function which (1) gets all recent secrets, (2) gets popular secrets, (3) gets count of all likes, (4) gets the current user based on session information, (5) get all current user secrets....
-- Modify your `login` & `registration` so the above function retrieves said data & passes to template (to show for dashboard).
"""
