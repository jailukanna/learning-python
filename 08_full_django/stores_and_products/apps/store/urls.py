"""stores_and_products application Configuration

Sets up URL patterns for `stores_and_products` application.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
