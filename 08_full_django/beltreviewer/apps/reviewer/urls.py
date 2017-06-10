"""reviewer URL Configuration

Sets up urls files for `reviewer` app.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # loads login/reg homepage
    url(r'^register$', views.register), # Validates and registers new User
]
