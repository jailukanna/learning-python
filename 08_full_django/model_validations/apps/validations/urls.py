"""validations application URL Configuration

Configures route patterns for `validations` assignment.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Loads homepage.
]
