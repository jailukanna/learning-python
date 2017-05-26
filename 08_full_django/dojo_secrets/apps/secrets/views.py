from django.shortcuts import render, redirect
from models import User, Secret # gives us access to `User` and `Secret` models
from django.contrib import messages # grabs django's `messages` module
from django.forms.models import model_to_dict # Let's us jsonify django model data for use in sessions
from . import dashboard # grab custom dashboard helper module

# Add extra message levels to default messaging to handle login or registration error generation:
# https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#creating-custom-message-levels
LOGIN_ERR = 50 # Messages level for login errors
REG_ERR = 60 # Messages level for registration errors
SECRET_ERR = 70 # Messages level for secret errors
LOGOUT_SUCC = 80 # Messages level for logout success messages


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
                # Reload index page:
                return redirect("/")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                print "Unexpected errors occurred."
                messages.add_message(request, REG_ERR, "An unexpected error has occurred.", extra_tags="reg_errors")
                return redirect("/")
        except KeyError:
            # If validation successful, create new user and load dashboard:
            print "User passed validation and has been created..."
            # Set session to validated User:
            print "Setting session data for logged in new user..."
            request.session["user_id"] = validated["logged_in_user"].id
            # Load dashboard and get dashboard data:
            return redirect("/dashboard")

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
                # Reload homepage:
                return redirect("/")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                print "Unexpected errors occurred."
                messages.add_message(request, LOGIN_ERR, "An unexpected error has occurred.", extra_tags="login_errors")
                return redirect("/") # Added for extra security to cover all cases.
        except KeyError:
            # If credentials are validated, set session, and load dashboard:
            print "User passed validation..."
            # Set session to validated User:
            print "Setting session data for logged in user..."
            request.session["user_id"] = validated["logged_in_user"].id
            # Fetch dashboard data and load dashboard page:
            return redirect("/dashboard")

    # If request method is not a POST, reload index as this is an unexpected request:
    else:
        print "Unexpected errors occurred."
        messages.add_message(request, LOGIN_ERR, "An unexpected error has occurred.", extra_tags="login_errors")
        return redirect("/")

def logout(request):
    """Logs out current user."""

    # Try deleting session and send success message:
    try:
        # Deletes session:
        del request.session['user_id']
        # Adds success message:
        messages.add_message(request, LOGOUT_SUCC, "Successfully logged out.", extra_tags="logout_succ")
    except KeyError: # If `user_id` is not found pass
        pass

    # Return to index page:
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
                # Redirect to dashboard route which gets dashboard data and loads dashboard page:
                return redirect("/dashboard")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                print "Unexpected errors occurred."
                messages.add_message(request, SECRET_ERR, "An unexpected error has occurred.", extra_tags="secret_errors")
                return redirect("/") # Added for extra security to cover all cases.
        except KeyError:
            #  If secret passes validation, and redirect to dashboard route which fetches dashboard data and loads dashboard:
            print "Secret passed validation and has been created."
            return redirect("/dashboard")

    # If request method is not POST, return to dashboard as this is an unexpected request:
    else:
        print "Unexpected errors occurred."
        messages.add_message(request, SECRET_ERR, "An unexpected error has occurred.", extra_tags="secret_errors")
        return redirect("/dashboard")

def delete(request, id):
    """
    Deletes secret by id.

    Parameters:
    - `id` - ID of a secret object to be deleted. Provided from template data.
    """

    print "Secret id to be deleted: {}".format(id)
    print "Deleting secret..."
    # Deletes secret by secret.id provided.
    Secret.objects.get(id=id).delete()
    print "Secret deleted."
    return redirect("/dashboard")

def get_dashboard_data(request):
    """
    Gets all dashboard data.

    Data Fetched for Dashboard:
    - `recent_secrets` - 3 most recent secrets
    - `popular_secrets` - 4 most popular secrets by likes
    - `logged_in_user` - currently logged in user
    """

    # Validate user session prior to fetching dashboard data:
    try:
        request.session["user_id"]
        print "User session validated."
        # Fetch dashboard data for template:
        print "Fetching dashboard data..."
        dashboard_data = dashboard.populate_data(request.session["user_id"])
        # Load dashboard and send dashboard data:
        return render(request, "secrets/dashboard.html", dashboard_data)
    except KeyError:
        # If session object not found, load index:
        print "User session not validated."
        return redirect("/")

def like(request, id):
    """
    Like a secret.

    Parameters:
    - `id` - ID of secret object to be liked.
    """

    try:
        # Get current logged in user:
        user = User.objects.get(id=request.session["user_id"])
        # Get current secret:
        secret = Secret.objects.get(id=id)
        print user.first_name
        print secret.description
        print "Liking secret..."
        # Add user to secret's `likes`:
        secret.likes.add(user)
        print secret.likes
        # Reload dashboard with updated dashboard data:
        return redirect("/dashboard")
    except KeyError:
        print "Unexpected errors occurred."
