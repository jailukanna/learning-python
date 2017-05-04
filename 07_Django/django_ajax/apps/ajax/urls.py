"""ajax application URL Configuration

This file controls the routes for the `ajax` application.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # loads index
    url(r'^message$', views.response), # loads response
]
