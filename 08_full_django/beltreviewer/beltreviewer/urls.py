"""beltreviewer URL Configuration

Sets up urls files for each application belonging to `beltreviewer` project.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.reviewer.urls")), # imports `reviewer` app urls
]
