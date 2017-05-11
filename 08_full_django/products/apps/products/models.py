from __future__ import unicode_literals

from django.db import models # accesses Djano `model` module

class Product(models.Model):
        name = models.CharField(max_length=30) # CharField is a "column type".
        description = models.CharField(max_length=200)
        price = models.DecimalField(max_digits=5, decimal_places=2) # DecimalField is a "column type".
        cost = models.DecimalField(max_digits=5, decimal_places=2)
        category = models.CharField(max_length=30)
        created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is a "column type".
        updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter.
