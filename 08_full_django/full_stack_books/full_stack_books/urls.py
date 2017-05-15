"""full_stack_books URL Configuration

Sets up URL configurations for any applications belonging to this project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.full_books.urls")), # pulls in URL patterns for `full_books` app
]
