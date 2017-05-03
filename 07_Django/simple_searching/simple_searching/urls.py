"""simple_searching URL Configuration

This file pulls in the `searching` app `urls.py` file in `/apps/searching/urls.py`. Please see that file for explicit routes for this application. Note: Because Django can have multiple apps inside of a singple project, it would be possible to use this page to forward various URLs to other applications. In this particular setup, we just do a simple catch-all and load up the appropriate view for the `searching` app.

"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.searching.urls")), # pulls in `/apps/searching/urls.py` file
]
