"""dojo_secrets URL Configuration

Sets up URL files for all applications in this project.

Current applications:
- `secrets` - This application allows users to create and interact with secr
ets.
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index), # load login/registration page
    url(r'^login$', views.login), # validate and login a user
    url(r'^logout$', views.logout), # logout a user
    url(r'^new_secret$', views.new_secret), # validate and make a new secret
    url(r'^delete/(?P<id>\d*)$', views.delete), # delete a secret
    url(r'^like/(?P<id>\d*)$', views.like), # like a secret
    url(r'^dashboard$', views.get_dashboard_data), # fetch dashboard data and load dashboard
]
