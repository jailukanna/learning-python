# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse # for sending json

def index(request):
    """Loads index page."""

    print "Running index method..."
    print "Loading index.html page..."
    return render(request, "ajax/index.html") # loads `./templates/ajax/index` page

def response(request):
    """Sends JSON response with message from server."""

    print "Running response method..."
    print "Sending reply..."
    reply = {
        "message": "This is the server talking 💬 Look ma, no refresh! AJAX baby! 🤘"
    }
    # Note: `JsonResponse` can only be used if the module at
    # the top of this document is imported. Simply provide
    # the dictionary file, or define a dictionary as a parameter,
    # ie, "JsonResponse({"key": value})"
    return JsonResponse(reply)
