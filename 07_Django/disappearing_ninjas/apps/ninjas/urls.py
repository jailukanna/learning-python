from django.conf.urls import url
from . import views # hooks us into to our views.py file (controller)

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ninjas$', views.ninjas),
	url(r'^ninjas/(?P<color>\b(orange)|(red)|(blue)|(purple)\b)$', views.ninja_color), # how can i make this case insensitive?,
	url(r'^ninjas/(?P<color>.*)$', views.ninja_color),
]
