from django.conf.urls import url
from . import views # imports views.py from the current working directory

urlpatterns = [
    url(r'^$', views.index)
]
