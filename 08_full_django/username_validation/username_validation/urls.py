"""username_validation URL Configuration

Sets up URL configurations for all applications in `username_validation` project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.validation.urls")), # URL patterns for `validation`
]
