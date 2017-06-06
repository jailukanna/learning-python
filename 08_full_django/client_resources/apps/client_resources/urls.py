"""client_resources app URL Configuration

This file sets up all url configuration files for all applications belonging to
this `client_resources` application.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Load client homepage (dashboard).
    url(r'^client/add$', views.add_client), # Load client add form (or create new client).
    url(r'^client/(?P<id>\d*)/$', views.show_client), # Load show client page.
    url(r'^(?P<id>\d*)/addproject/$', views.add_project), # Load project add form (or create new project for client).
    url(r'^show/projects/(?P<id>\d*)$', views.show_project), # Load show project page.
]
