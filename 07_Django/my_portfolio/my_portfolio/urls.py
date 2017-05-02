"""my_portfolio URL Configuration

Directs urls to `apps/portfolio/urls.py` file. See the aforementioned file for
actual application routes.
"""

from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.portfolio.urls")),
]
