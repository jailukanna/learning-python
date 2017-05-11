from django.conf.urls import url
from . import views # '.' means from current folder, yes?

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogs$', views.blogs),
    url(r'^comments/(?P<id>\d+)$', views.comments), # looks for any number of digits (\d) reocurring (+)
]