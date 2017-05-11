from django.shortcuts import render
from models import Product

# Create 3 Different Products:
"""
Note: You can see our object creation has been placed outside of our `index()`
method. This is because if we placed these creation events inside of our index method,
we'd have the same product created on every refresh.
"""

Product.objects.create(name="Kool Aid",description="A powdered sugary drink.",price="1.00",cost="0.50",category="Beverage")
Product.objects.create(name="Lentil Burger",description="Lentils, onions and shallots pressed into a patty.",price="8.00",cost="3.50",category="Food")
Product.objects.create(name="French Fries",description="Organic potatos fried to a crisp and seasoned to perfection.",price="2.00",cost="1.00",category="Food")

def index(request):
    """Loads homepage."""
    print "Loading homepage..."
    print "Building instance off of `Product` model..."


    # Stores all products:
    products = Product.objects.all()

    # Loop through products and print information:
    print "/////////////    P R O D U C T S    /////////////"
    for product in products:
        print "- {} | {} | ${} (consumer cost)/ea | ${}/ea (business cost)".format(product.name, product.description, product.price, product.cost)
    print "/////////////////////////////////////////////////"

    return render(request, "products/index.html")
