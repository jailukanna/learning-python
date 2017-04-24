from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), #make sure to include the $ in your app urls.py
    url(r'^users$', views.show),
    url(r'^create_user$', views.create),
]