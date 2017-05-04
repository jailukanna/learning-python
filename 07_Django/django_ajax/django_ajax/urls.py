"""django_ajax URL Configuration

This file loads the URL patterns for any apps in this project.

Current applications:
-'ajax' - see `./../apps/ajax` for application. Please see `./../apps/ajax/urls.py`
for routes.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.ajax.urls")), # loads `urls.py` for `ajax` application
]
