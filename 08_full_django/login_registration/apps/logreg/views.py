# Import dependencies:
from django.shortcuts import render, redirect # Render templates and redirect routes.
from models import User # Gives us access to `User` model
import bcrypt # grabs bcrypt module for encrypting and decrypting passwords

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
        validated = User.objects.login_validate(request) # pass entire request object as we need this for creating django-messages
        # If errors, load homepage with errors:
        if validated == False:
            print "User could not be logged in."
            # We must render, not redirect, so `request` object gets updated with django messages:
            # If we redirect, the request object is updated and our old modified one with the messages is lost.
            return render(request, "logreg/index.html")
        # If credentials are validated, load success page along with `logged_in_user`:
        else:
            # Return success page with the validated user.
            return render(request, "logreg/success.html", validated)

    # If request method is "GET", load homepage:
    return render(request, "logreg/index.html")

def register(request):
    """Validates, and if successful, creates a new `User`."""

    # If request method is "POST", begin validate form then create user if validation successful:
    if request.method == "POST":
        print "Validating registration form..."
        # Validate registration data submitted from registration form:
        validated = User.objects.register_validate(request) # see `./models.py`, `register_validate()`
        # If errors, reload index page (Django will load error objects):
        if validated == False:
            print "User could not be registered."
            # Send back index with updated request object (which contains our error messages via Django messaging):
            # Note: If we did a `redirect` to our index route, our django message data would not display,
            # as it is stored in the updated request object.
            return render(request, "logreg/index.html")
        # If validation successful, create new user and send it along with success page:
        else:
            # Load success page with `validated` user (already returned as a `dict` obj.)
            return render(request, "logreg/success.html", validated)

    # If request route on `/register` is "GET", redirect to index (not a function in our application but security for our route):
    elif request.method == "GET":
        # Redirect to homepage:
        return redirect('/')
