"""portfolio app URL Configuration

This file captures routes for our Django application and defines the methods
in the `views.py` file which handles them.
"""
from django.conf.urls import url
from . import views # imports `views.py` file from this directory

urlpatterns = [
    url(r'^$', views.index), # index route
    url(r'^projects$', views.projects), # loads index page
    url(r'^about$', views.about), # loads about page
    url(r'^testimonials$', views.testimonials), # loads testimonials page
]
