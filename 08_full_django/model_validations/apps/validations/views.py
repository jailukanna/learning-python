# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render # `render` module allows us to render Templates.
from models import User # allows us to access our `User` model

def index(request):
    """Loads homepage."""

    # The following lines of code are commented out so that I can instead utilize the Django Shell,
    # rather than have object creation with each and every index request. This is only for development purposes,
    # and in a real application, a route would fulfill object creation (however, this route would not be the index route).

    """
    # Register a new user with an email and name.
    data = {
        "email" : "tim@sasquat.ch",  # or request.POST.get('email')
        "name" : "Tim Knab",  # or request.POST.get('name')
    }
    tim = User.objects.register(**data)
    # Note, you must add the TWO ASTERISKS ** to your DICTIONARY that you send, in order for kwargs to work properly.
    # If you send only a dictionary, without the two asterisks, it won't work.
    # If you send an object type other than a dictionary (like a list or strings), it wont' work.
    # What you send must be a DICTIONARY with **TWO ASTERISKS PRECEEDING IT!
    """
    return render(request, "validations/index.html")
