"""landscapes URL Configuration

Imports `urls.py` for various apps. In this application, so far there is only one app called `landscape`. Please see `./../apps/landscape/urls.py` for the exact urls in this application.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.landscape.urls")),
]
