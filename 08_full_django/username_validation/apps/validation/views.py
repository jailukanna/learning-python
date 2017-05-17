from django.shortcuts import render
from models import User

def index(request):
    """Loads login page."""

    # If 'POST' method, begin user login:
    if request.method == "POST":
        # Prepare data for `User` validation / creation:
        user_data = {
            "username": request.POST["username"],
        }
        # Validate user:
        validation_errors = User.objects.validate(**user_data)
        print "///// VALIDATION OBJECT //////"
        print validation_errors
        print len(validation_errors)
        print "//////////////////////////////"
        # If any errors, send back errors with index page:
        if len(validation_errors) > 0:
            print "Error validating username."
            # Prepare errors object:
            errors = {
                "errors" : validation_errors
            }
            # Send index page along with errors:
            return render(request, "validation/index.html", errors)
        # If no errors, return success page with new user and all current users:
        else:
            print "Username validation passed."
            # Create new user:
            new_user = User(username=request.POST["username"])
            # Save new User:
            new_user.save()
            # Prepare new User object:
            success = {
                "logged_in_user": new_user, # new user
                "all_users": User.objects.all(), # all users
            }
            return render(request, "validation/success.html", success)


    elif request.method == "GET":
        # Load index page:
        return render(request, "validation/index.html")
