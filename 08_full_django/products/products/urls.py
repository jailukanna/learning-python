"""products URL Configuration

Sets up URL configuration for each application in the `products` project.

Current Applications:
-`products`: a simple app to play with Django Models and creating and retrieving data.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.products.urls")),
]
