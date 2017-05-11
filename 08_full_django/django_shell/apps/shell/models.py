from __future__ import unicode_literals
# imports Django's models module (say that three times fast):
from django.db import models

# Our Super Basic Model.
# Note: When we create our model properties, we have to define a "column type".

class People(models.Model):
        first_name = models.CharField(max_length=30) # CharField is a "column type".
        last_name = models.CharField(max_length=30)
        created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is a "column type".
        updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter.
