"""dojo_secrets URL Configuration

Sets up URL files for all applications in this project.

Current applications:
- `secrets` - This application allows users to create and interact with secr
ets.
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^new_secret$', views.new_secret),
]
