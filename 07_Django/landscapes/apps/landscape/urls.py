"""landscape app URL Configuration

URL configuration for `landscape` app.
URLs:
    - '/' - loads index.html.
    - '(?P<integer>([1-9]|[1-4]\d|50))' - this route parameter does a few things, first, it checks for a parameter (thus the `?P`), and is looking for any `<integer>` which matches our regex pattern. Our regex pattern, broken down as follows: `[1-9]` checks first for any integers 1-9. The `|` indicates `OR`, followed by `[1-4]\d|50`. This second statement allows for 2 integer place holders. The first being `1-4`, to handle the powers of then such as 10, 20, 30 and 40, followed by `\d|50`, as the second integer placeholder. `\d` allows for any number `0-9` thus, 11, 12, 13 ... 49 will now be accepted. The second `|` is another `OR` operator, followed by `50` which matches for literally the value of 50. Without the `|50` in the pattern, only the integers 1-49 would match. By adding `|50`, we're saying, "or 50", making it inclusive in our matching (phew, what a mouthful!).
"""
from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.index), # loads index.html
            url(r'^(?P<integer>([1-9]|[1-4]\d|50))$', views.scene), # loads scene.html
            ]
