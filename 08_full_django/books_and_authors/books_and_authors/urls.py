"""books_and_authors URL Configuration

Sets up URL configurations for any applications tied to the `books_and_authors` project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.authors.urls")),
]
