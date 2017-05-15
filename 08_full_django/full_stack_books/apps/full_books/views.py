# Import dependencies:
from django.shortcuts import render, redirect # allows us to render Templates and redirect
from models import Book # gives us access to `Book` model

def index(request):
    """Retreives all books and loads homepage."""

    all_books = {
        "all_books": Book.objects.all().order_by("-created_at")
    }
    return render(request, "full_books/index.html", all_books) # loads `index.html` and sends `all_books`

def create_book(request):
    """Creates new books."""

    # If method is post:
    if request.method == "POST":
        # Capture Book Data from Form as Dictionary (for validation/creation purposes):
        book_data = {
            "title": request.POST['title'],
            "category": request.POST['category'],
            "author": request.POST['author']
        }
        # Validate or Create New Book:
        new_book = Book.objects.create_book(**book_data) # will return either a list of errors or a new book
        """
        Note: regarding the parameter `**book_data` in the method above:
        The double asterisks are required for the `**kwargs` parameter to work as intended.
        Additionally, the "book_data" object must be a dicationary.
        **str or **list, etc, will not work. Only **dict.
        """
        # Check if any errors in new book:
        try:
            print new_book["errors"]
            print "Errors creating new book."
            # Print errors to server console:
            print "////// ERRORS ///////"
            for error in new_book['errors']:
                print error
            print "/////////////////////"
            # Setup Errors list and All Books (to populate our table) for Template:
            book_data = {
                "errors": new_book['errors'],
                "all_books": Book.objects.all().order_by("-created_at"),
            }
            # Load template with errors and all_books:
            return render(request, "full_books/index.html", book_data)
        # If no errors:
        except TypeError:
            # Reload homepage (which will pull in all books including new one):
            return redirect('/')
    # If not a post method:
    else:
        redirect('/') # return to index
