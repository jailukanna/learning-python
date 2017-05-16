"""courses Application Configuration

Sets up URL patterns for any courses belonging to this project.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # Loads homepage.
    url(r'^courses/destroy/(?P<id>\d+)/$', views.destroy), # Loads delete confirmation page or destroys depending on request method.
]
