from django.conf.urls import url
from . import views # '.' means current directory, yes?

urlpatterns = [
    url(r'^$', views.index),
]
