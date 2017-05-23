"""dojo_secrets URL Configuration

Sets up URL files for all applications in this project.

Current applications:
- `secrets` - This application allows users to create and interact with secrets.
"""
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include("apps.secrets.urls")),
]
