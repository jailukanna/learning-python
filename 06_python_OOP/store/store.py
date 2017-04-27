class Store(object):
    """Create a new `Store` instance.

    Notes:
    `object` parameter is required. `__init__` instance method below is required
    and is used as Constructor. `self` is required for all instance methods so
    that they may reference themselves.
    """

    def __init__(self, location=None, owner=None):
        """Store constructor function.

        Parameters:
        self -- refers to this instance, allows us class to access itself (default = self)
        location -- user entered store location (default = None)
        owner -- name of store owner (default = None)
        """

        self.products = []; # array to hold products
        self.location = location # user entered location
        self.owner = owner # user entered owner first and last name

    def add_product(self, name, quantity):
        """Add product to products array.

        Parameters:
        name -- user entered name of product to add (No default setting, required).
        quantity -- user entered quantity of product to add (No default setting, required).
        """

        # Append product to `products` array
        self.products.append({
            'name': name,
            'quantity': quantity,
        })
        return self

    def remove_product(self, product_name):
        """Remove product from products array by product name.

        Parameters:
        product_name -- user entered name of product to remove (No default setting, required).
        """

        # Set a `found variable`:
        found = False
        for idx in range(len(self.products)): # loop self.products
            if self.products[idx]['name'] == product_name: # match for product_name
                del self.products[idx] # remove matching dict by idx
                found = True
                break # exit out of for loop

        if found == False:
            print 'Product "{}" not found in Inventory.'.format(product_name)
        return self

    def inventory(self):
        """List all products and relevant information."""

        for product in self.products:
            # First portion of print statement: Get index value of product and
            # convert to string. Second portion is to print product dictionary.
            print '## '+str(self.products.index(product))+' ##:', product
        return self

# Invoke instance of Store:
new_store = Store('02301 SW 351ST ST, GANESH, WA 98088', 'Timothy William Knab')
print new_store.location # prints location above
print new_store.owner # prints name in parameter above

# Invoke `add_product()` instance method:
new_store.add_product('Candles', 10)
new_store.add_product('Bubble Gum', 50)
new_store.add_product('Oranges', 500)
print new_store.products
# above prints: [{'name': 'Candles', 'quantity': 10}, {'name': 'Bubble Gum', 'quantity': 50}, {'name': 'Oranges', 'quantity': 500}]

# Invoke `remove_product()` instance method:
new_store.remove_product('Candles')
new_store.remove_product('Bobbleheads')
# Check if `Candles` is now missing:
print new_store.products
# above prints: [{'name': 'Bubble Gum', 'quantity': 50}, {'name': 'Oranges', 'quantity': 500}]

# Invoke `inventory()` instance method:
new_store.inventory()
# Prints:
## 0 ##: {'name': 'Bubble Gum', 'quantity': 50}
## 1 ##: {'name': 'Oranges', 'quantity': 500}
