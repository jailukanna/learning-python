"""login_registration URL Configuration

Sets up all URL configurations for all applications belonging to `login_registration` project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.logreg2.urls")), # Grabs `urls.py` from `./../apps/loginreg2` application
]
