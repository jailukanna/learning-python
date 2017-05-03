"""surprise URL Configuration

Maps routes for the `surprise` application. See `./views.py` for the corresponding methods for each route.
"""
from django.conf.urls import url
from . import views # imports `./views.py`

urlpatterns = [
    url(r'^$', views.index), # loads index page
    url(r'^surprise$', views.get_surprise), # shuffles string list and loads results page
]
