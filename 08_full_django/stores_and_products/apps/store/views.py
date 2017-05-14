# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render # Allows us to render templates
from models import Product, Store # Gives us access to our models

"""
Note: The Django ORM commands below are commented out so that every time the server
runs, new objects are not created. Please open the django shell via `python manage.py shell`,
once inside the shell, load your models via `from apps.store.models import Store, Product`.
Once models are loaded, you can copy and paste all of the ORM statements below into the shell.
"""

# # Create 5 stores:
# costco = Store(name="Costco", address="1234 Maple Street, New York, New York City 10023") # Store 1
# costco.save()
# kmart = Store(name="K-Mart", address="4392 Washington Lane, Seattle, Washington 98011") # Store 2
# kmart.save()
# target = Store(name="Target", address="7849 Ford Street, Chicago, Illinois 60031") # Store 3
# target.save()
# pcc = Store(name="PCC", address="103200 Arlington Street, Bothell, Washington 98011") # Store 4
# pcc.save()
# chaco = Store(name="Chaco Canyon", address="1423 Centennial Street, Seattle, Washington 98004") # Store 5
# chaco.save()

# # Create 5 products:
# soap = Product(name="Dawn Soap", description="Sudsy soap for your needs.", price="2.00", cost="0.50", category="Cleaning") # Product 1
# soap.save()
# sponge = Product(name="Braxo Sponge", description="A sponge for scrubbing.", price="0.50", cost="0.10", category="Cleaning") # Product 2
# sponge.save()
# bucket = Product(name="Plastic Wash Bucket", description="Bucket for scrubbing or mopping.", price="10.50", cost="3.00", category="Cleaning") # Product 3
# bucket.save()
# lentil_burger = Product(name="Vegan Lentil Burger", description="A delightful lentil burger.", price="7.50", cost="2.10", category="Food") # Product 4
# lentil_burger.save()
# vegan_pizza = Product(name="Vegan Gluten Free Pizza", description="A non-dairy non-gluten pizza guaranteed to blow your mind.", price="2.50", cost="1.00", category="Food") # Product 5
# vegan_pizza.save()

# # The first 2 stores you created should both carry products 1,2 and 3:
# soap.store.add(costco)
# soap.store.add(kmart)
# sponge.store.add(costco)
# sponge.store.add(kmart)
# bucket.store.add(costco)
# bucket.store.add(kmart)

# # Stores number 3 and 4 should carry products 3,4, and 5:
# bucket.store.add(target)
# lentil_burger.store.add(target)
# vegan_pizza.store.add(target)
# bucket.store.add(pcc)
# lentil_burger.store.add(pcc)
# vegan_pizza.store.add(pcc)

# # The last store should carry all 5 products:
# soap.store.add(chaco)
# sponge.store.add(chaco)
# bucket.store.add(chaco)
# lentil_burger.store.add(chaco)
# vegan_pizza.store.add(chaco)

# # Get all products for all stores:
# costco.product_set.all()
# kmart.product_set.all()
# target.product_set.all()
# pcc.product_set.all()
# chaco.product_set.all()

# # Print stores for all products:
# soap.store.all()
# sponge.store.all()
# bucket.store.all()
# lentil_burger.store.all()
# vegan_pizza.store.all()


def index(request):
    """Loads homepage."""

    return render(request, "store/index.html")
