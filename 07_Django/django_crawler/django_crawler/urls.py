"""django_crawler URL Configuration

This file grabs each `urls.py` file for any respective applications inside of `./../apps`.

Current Apps:
    - `crawler` - a Django powered web crawler.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.crawler.urls")), # imports `urls.py` from `./../apps/crawler/urls.py
]
