"""surprise_me URL Configuration

Imports `apps/surprise/urls.py` file, which is what handles the routes for the `surprise`app. You may choose to add more to this file later, if you develop a second app to attach to this project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.surprise.urls")), # imports `./../apps/surprise/urls.py`
]
