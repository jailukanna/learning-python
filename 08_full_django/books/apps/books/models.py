from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50) # CharField is field type for characters
    author = models.CharField(max_length=50)
    publish_date = models.DateField(auto_now=False,auto_now_add=False) # DateField field type for date (not time)
    category = models.CharField(max_length=50)
    in_print = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
