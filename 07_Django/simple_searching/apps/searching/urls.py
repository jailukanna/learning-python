"""searching app URL Configuration

Sets up route URLs for the `searching` application. Each URL directs to a different method (located in `./views.py`). To see how each route behaves, please see the appropriate method in the views file for the individual route below. 
    
"""
from django.conf.urls import url
from . import views # imports `views.py` file from current directory

urlpatterns = [
    url(r'^$', views.index), # root route - loads index page
]
