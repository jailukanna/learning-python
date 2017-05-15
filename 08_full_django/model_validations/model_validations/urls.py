"""model_validations URL Configuration

Configures URLs for all applications in `model_validations` project.

Current Application:
-`validations` - Appication which allows us to experiment with Managers for our models (to utilize validaitons).
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.validations.urls")), # imports URL configuration for our `validations` application
]
