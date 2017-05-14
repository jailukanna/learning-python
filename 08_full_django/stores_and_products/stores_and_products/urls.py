"""stores_and_products URL Configuration

Sets up URL configuration files for any applications belonging to this project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.store.urls")),
]
