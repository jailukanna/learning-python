"""django_shell URL Configuration

Sets up application URLS for `django_shell` project.

Current Applications:
-`shell` - This application lets us explore the django shell and interact with Django Models.

"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.shell.urls")),
]
