"""courses URL Configuration

Sets up URL configurations for any applications belonging to this project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^',include("apps.courses.urls")), # imports urls.py for `courses` application
]
