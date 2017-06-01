"""
URL configurations for all apps in this project.

Current apps:
- `interests` - app which stores user interests
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.interests.urls")), # interests app
]
