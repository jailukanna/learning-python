# Import dependencies:
from django.shortcuts import render, redirect # Render templates and redirect routes.
from models import User # Gives us access to `User` model

def index(request):
    """Loads index page which is a login/registration page."""

    # If request method is a "POST", begin process of validating credentials logging user in:
    if request.method == "POST":
        # Prepare data as dict for validation:
        login_data = {
            "email": request.POST["login_email"],
            "password": request.POST["login_password"] # would normally bcrypt password here
        }
        # Validate credentials:
        validate = User.objects.login_validate(**login_data)
        # If errors, load homepage with errors:
        if len(validate["login_errors"]) > 0:
            print "Errors logging in user."
            return render(request, "logreg/index.html", validate)
        # If credentials are validated, load success page with logged in user:
        else:
            # Prepare logged_in_user data for Template:
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
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "confirm_pwd": request.POST["confirm_pwd"],
        }
        # Validate registration data:
        # Note: `**` along with dict obj must be included for `register_validate(**kwargs)` function
        validate = User.objects.register_validate(**register_data) # see `./models.py`, `register_validate()`
        # If errors, send back errors and index page:
        if len(validate["reg_errors"]) > 0:
            print "Errors validating user registration..."
            print validate
            # Send errors data along with Template:
            return render(request, "logreg/index.html", validate)
        # If no validation errors, create new user and load success page:
        else:
            print "Registration data passed validation..."
            print "Creating new user...."
            print "Hashing password...."
            ## No password hashing in this project, but you'd do it here by calling your `UserManager` class again.
            # Create new user (as dict object) to make it ready for Template:
            logged_in_user = {
                "logged_in_user": User(first_name=register_data['first_name'], last_name=register_data['last_name'], email=register_data['email'], password=register_data['password']),
            }
            # Save new `User`:
            logged_in_user["logged_in_user"].save()
            # Load success page with `logged_in_user` dictionary
            return render(request, "logreg/success.html", logged_in_user)

    # If request route on `/register` is "GET", redirect to index (not a function in our application but security for our route):
    elif request.ethod == "GET":
        # Redirect to homepage:
        return redirect('/')
