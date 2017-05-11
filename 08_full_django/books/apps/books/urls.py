"""books app URL Configuration

Defines URL patterns for `books` application.
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
