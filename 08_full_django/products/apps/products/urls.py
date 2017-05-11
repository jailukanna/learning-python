"""products application Configuration

Defines URL patterns accepted in the `products` application.

Current URLS:
-`/`: loads homepage.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # loads homepage
]
