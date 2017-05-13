# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models # imports Django's `models` module for managing and building Models.

"""
Builds `Author` and `Anthology` Django Models.

Note: In the models below, we've established a Many-to-Many relationship between `Author` and `Anthology`.
Because an Anthology is a collection of works from many authors, one anthology may contain many authors.

See more about Many-to-Many relationships here:
https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/
"""

class Anthology(models.Model):
    """Builds a single `Anthology`, with a title and publish date."""
    title = models.CharField(max_length=50)
    publish_date = models.DateField(auto_now=False,auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    """Builds a single `Author`, with a  name, DOB, and a field for all anthologies to which the author belongs."""
    name = models.CharField(max_length=50) # CharField is field type for characters
    dob = models.DateField(auto_now=False,auto_now_add=False) # DateField field type for date (not time)
    anthologies = models.ManyToManyField(Anthology) # Ties us into `Anthology` model: Many anthologies may contain many authors.
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter.
