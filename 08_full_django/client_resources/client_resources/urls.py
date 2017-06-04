"""client_resources URL Configuration

This file sets up all url configuration files for all applications belonging to
this `client_resources` application.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.client_resources.urls")),
]
