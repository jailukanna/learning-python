"""URL configurations for `interests` app."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # loads homepage
    url(r'^add$', views.add), # add a user interest
    url(r'^users$', views.users), # show all current users
    url(r'^show/(?P<id>\d*)$', views.show), # show user's interests
]
