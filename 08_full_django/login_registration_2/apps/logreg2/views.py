# Import dependencies:
from django.shortcuts import render, redirect # Render templates and redirect routes.
from models import User # Gives us access to `User` model
from django.contrib import messages # grabs django's `messages` module

# Add extra message levels to default messaging to handle login or registration error generation:
# https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#creating-custom-message-levels
LOGIN_ERR = 50 # Messages level for login errors
REG_ERR = 60 # Messages level for registration errors

def index(request):
    """Loads index page which is a login/registration page."""

    # If request method is a "POST", begin process of validating credentials logging user in:
    if request.method == "POST":
        """
        # Note:
        I don't know if it's bad to pass the entire request
        object along like I did below. The only reason I did this, was because in
        order to use Django's `messaging` module, one of the required
        arguments was the `request` object, as it uses the request object to attach
        the messages to.

        *If* it was bad to do this for performance or memory reasons,
        another strategy might be to return a list of errors from the manager,
        and then iterate over the errors here in `views.py` generating the official
        Django messages errors. However, for simplicity, you might just choose to display
        that manually as well.

        Overall, my choice above was made in order to do all validations, all
        error message generation, and all object creation or retrieval in my Manager,
        and not my `views.py`
        """
        # Validate credentials submitted to login form:
        # Note: Returns validated user if passes validations, otherwise returns `False`.
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
                return render(request, "logreg2/index.html")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                return redirect('/') # Added for extra security to cover all cases.
        # If credentials are validated, load success page along with `logged_in_user`:
        except KeyError:
            # Return success page with the validated user.
            return render(request, "logreg2/success.html", validated)

    # If request method is "GET", load homepage:
    return render(request, "logreg2/index.html")

def register(request):
    """Validates, and if successful, creates a new `User`."""

    # If request method is "POST", begin validate form then create user if validation successful:
    if request.method == "POST":
        print "Validating registration form..."
        # Validate registration data submitted from registration form:
        """
        Note: Double asterisks `**` must be included along with dict obj below for
        the `register_validate(**kwargs)` function to work. This function either
        returns `False` if validation fails, or returns validated user data with
        the password now encrypted and ready for creation.
        """
        # Prepare registration data for validation:
        reg_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "confirm_pwd": request.POST["confirm_pwd"],
        }
        validated = User.objects.register_validate(**reg_data) # see `./models.py`, `register_validate()`
        # If errors, reload index page (Django will load error objects):
        try:
            if len(validated["errors"]) > 0:
                print "User could not be registered."
                # Generate Django errors:
                for error in validated["errors"]:
                    # Add error to Django's error messaging:
                    messages.add_message(request, REG_ERR, error, extra_tags="reg_errors")
                # Send back index with updated request object (which contains our error messages via Django messaging):
                # Note: If we did a `redirect` to our index route, our django message data would not display,
                # as it is stored in the updated request object.
                return render(request, "logreg2/index.html")
            else:
                # If this is firing, it means errors returned, but they weren't expected.
                # Could mean someone is spoofing your URL request.
                return redirect('/') # Added for extra security to cover all cases.
        # If validation successful, create new user and send it along with success page:
        except KeyError:
            # Load success page with `validated` user (already returned as a `dict` obj.)
            return render(request, "logreg2/success.html", validated)

    # If request route on `/register` is "GET", redirect to index (not a function in our application but security for our route):
    elif request.method == "GET":
        # Redirect to homepage:
        return redirect('/')
