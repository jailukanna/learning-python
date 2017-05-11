from django.shortcuts import render
from models import Book, Author


# Practice Creating a Author:
julianna = Author.objects.create(name="Julianna Giles",DOB="1988-07-02")
julianna.save()
tim = Author.objects.create(name="Tim Knab",DOB="1984-09-26")
tim.save()
print julianna.name
print tim.name

# Practice Creating a Book:
her_book = Book.objects.create(title="Her New Book", author_id=julianna, publish_date="2001-01-01", category="Natural Medicine")
my_book = Book.objects.create(title="Tim's New Book", author_id=tim, publish_date="2001-01-01", category="Ecology")
her_book.save()
print her_book.title, her_book.author_id.name, her_book.author_id.id

def index(request):
    print "Loading homepage..."

    # Get all authors and books:
    authors = Author.objects.all()
    books = Book.objects.all()

    # Prepare dictionary for Template:
    author_book_data = {
        "authors" : authors,
        "books" : books
    }

    # Render index page and export author and book data to Template:
    return render(request, "authors/index.html", author_book_data)
