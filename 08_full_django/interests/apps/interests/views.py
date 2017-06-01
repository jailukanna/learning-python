# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User, Interest
from django.contrib import messages # grabs django's `messages` module

def index(request):
    """Load user interest creation page."""

    # Load hompage:
    return render(request, "interests/index.html")

def add(request):
    """Adds a new user interest."""

    if request.method == "POST":
        """
        Check if user exists, and if so, checks if interest already exists. If
        user exists, but interest does not, will create a new interest for that user.
        If user does not exist, will create a new user and a new interest for that
        user:
        """

        # Prepare data for validation/creation events:
        user_interest_data = {
            "name": request.POST["name"],
            "interest": request.POST["interest"],
        }
        # Validate above data. Note: If successful, user is returned.
        validated = User.objects.validate(**user_interest_data)
        if type(validated) is list:
            # Generate errors:
            for error in validated:
                messages.error(request, error)
            return redirect('/')
        else:
            # User interest has been validated, get all users and load users page:
            return redirect('/users')
    else:
        # An unexpected request has occurred:
        return redirect('/')

def users(request):
    """Shows all users."""

    all_users = {
        "all_users": User.objects.all()
    }
    return render(request, "interests/users.html", all_users)

def show(request, id):
    """
    Shows individual user's interests.

    Parameters:
    - `id` - ID of user whose interests to show.
    """

    print id
    # Get user based on ID:
    user = {
        "user": User.objects.get(id=id),
        "interests": User.objects.get(id=id).interests.all()
    }
    return render(request, "interests/show.html", user)
