from django.conf.urls import url
from . import views # imports views.py file

urlpatterns = [
    url(r'^$', views.index), # will load index method in views file
]
