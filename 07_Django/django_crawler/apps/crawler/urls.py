"""crawler URL Configuration

This application is designed to crawl websites and gather data, returning the data and displaying it to your template.
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # loads index.html page
]
