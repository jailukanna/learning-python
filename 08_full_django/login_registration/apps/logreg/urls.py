"""logreg app URL Configuration

Sets up all URL routes for `logreg` application.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Loads login/registration homepage
    url(r'^register$', views.register), # Validates and registers new User
]
