"""username_validation URL Configuration

Sets up URL configurations for all applications in `username_validation` project.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Loads homepage
]
