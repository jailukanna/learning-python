"""authors URL Configuration

Setup URL patterns for `authors` application.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.index), # loads homepage 
                ]
