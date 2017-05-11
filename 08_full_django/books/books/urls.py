"""books URL Configuration

Sets up URL configurations for each application in this project.

Current applications:
-`books`: application which practices django ORM methods to create and edit a books model.
"""

from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.books.urls")),
]
