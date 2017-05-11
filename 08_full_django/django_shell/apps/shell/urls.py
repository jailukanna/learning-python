"""shell app URL Configuration

Sets up application URL patterns for the `shell` application.
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
