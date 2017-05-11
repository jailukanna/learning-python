# Setup our dependencies:
from django.shortcuts import render # allows us to render Templates
from models import Book # gives us access to `Book` model

# Create 5 instances of Books model:
"""
Note: Because you are manually creating discrete objects in `views.py`, if you
*restart* your server, an additional iteration of object creation will take place.
That is to say, your 5 items will become 10, and if you restart your server again,
the number will go to 15.

This is only to be a likely scenario in development, and not in production, as
most object creations are tied to form data and routes related to form submission.
However, it's something to be mindful.

To Erase Objects:
If you needed to clear out all of your model Objects in the event that duplicates
were created, you can enter the following command to do so:

`python manage.py shell` # loads Django shell
`from apps.books.models import Book` # Loads your models.
`Book.objects.all().delete()` # this will delete all entries.
"""
Book.objects.create(title="Brave New World",author="Aldous Huxley",publish_date="1932-01-01",category="Science Fiction",in_print="True")
Book.objects.create(title="Nineteen Eighty-Four",author="George Orwell",publish_date="1949-06-08",category="Science Fiction",in_print="True")
Book.objects.create(title="Wyoming Feathers",author="Bill Banks",publish_date="2011-01-01",category="Drama",in_print="False")
Book.objects.create(title="Tips From The Road",author="Bill Banks",publish_date="2020-01-01",category="Comedy, Travel",in_print="False")
Book.objects.create(title="Plants of the Pacific Northwest",author="Cary Conifer",publish_date="2015-01-01",category="Biology",in_print="True")

def index(request):
    """Loads homepage."""

    # Retrieve all books that have been created:
    books = Book.objects.all()

    # Setup dictionary for data for Template:
    book_data = {
        "books": books,
    }

    # Iterate over books and print to server console:
    for book in books:
        print book.title, book.author, book.publish_date, book.category

    return render(request, "books/index.html", book_data)
