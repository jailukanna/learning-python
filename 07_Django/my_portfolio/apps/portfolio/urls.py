"""portfolio URL Configuration

Contains the url patterns which are to be caught by the server, and defines the
methods (in `views.py`) which handles them.
"""
from . import views # imports views.py file which handles methods attached to routes

from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.index), # directs to index() method in `./views.py`
    url(r'^testimonials$', views.testimonials), # directs to index() method in `./views.py`
]
