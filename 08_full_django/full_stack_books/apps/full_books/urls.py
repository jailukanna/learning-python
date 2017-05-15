"""full_books URL Configuration

Sets up URL patterns for `full_books` application.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), # pulls in URL patterns for `full_books` app
    url(r'^create$', views.create_book), # validates and creates book (or returns errors)
]

"""
Notes for Improvement: You could improve this project by only using 1 route, rather than 2,
and using a `if request.method == "POST" or if request.method == "GET"` to
check and act accordingly. For now, we won't undo what we've done, but something
to consider and understand for the future.
"""
