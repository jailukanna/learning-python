"""real_portfolio URL Configuration

This file actually imports the `./../apps/portfolio/urls.py` file. Please see
that file for the actual routes that are caught by this Django application.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.portfolio.urls")), # imports `urls.py` file from `./../apps/portfolio`
]
