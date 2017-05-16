# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# class CourseManager(models.Manager):
#     """
#     Extends `Manager` methods with `add()` method below.
#
#     Parameters:
#     -`models.Manager` - Gives us access to the `Manager` method to which we append additional custom methods.
#     """
#
#     def add(self, **kwargs):
#         """
#         Runs validations and creates new course.
#
#         Parameters:
#         -`self` - Instance to whom this method belongs.
#         -`**kwargs` - A dictionary of book data accompanied by two asterisks (mandatory)
#         """
#
#         return None

class Course(models.Model):
    """
    Creates instances of a `Course`.

    Parameters:
    -`models.Model` - Django's `models.Model` method allows us to create new models.
    """

    name = models.CharField(max_length=50) # CharField is field type for characters
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
    # objects = CourseManager() # Attaches `CourseManager` methods to our `Course.objects` object.
