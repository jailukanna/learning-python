# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Store(models.Model):
    """
    Builds a single `Store`, with a name and address.

    Note: No field is necessary for `Store` as long as we are using the the
    `ManyToManyField` in a model which points to it (see `store` property in `Product` model below).
    """

    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    """Builds a product with a name, description, price, cost, category and stores many-to-many relationship with `Stores`"""

    name = models.CharField(max_length=30) # CharField is a "column type".
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2) # DecimalField is a "column type".
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=30)
    store = models.ManyToManyField(Store) # Ties us into `Store` model: Many stores may contain many products.
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is a "column type".
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter.
