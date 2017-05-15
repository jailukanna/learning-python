# Import dependencies:
from __future__ import unicode_literals
from django.db import models

class BookManager(models.Manager):
    """
    Extends `Manager` methods to include `__validate()` and `create_book()` methods below.

    Note: You must be sure to invoke this class inside of your `Book` model as `objects`.

    Parameters:
    -`models.Manager` - Gives us access to the `Manager` method to which we append additional custom methods.
    """

    def __validate(self, **kwargs):
        """
        Runs validations on new books.

        Parameters:
        -`self` - Instance to whom this method belongs.
        -`**kwargs` - A dictionary of book data accompanied by two asterisks (mandatory)
        """

        # Create an empty errors list:
        errors = []

        #--------------------------------------#
        #---- VALIDATE ALL FIELDS REQUIRED: ---#
        #--------------------------------------#
        # If all fields are not filled out:
        if len(kwargs) < 3:
            print "Error: All fields have not been submitted."
            # Add error to errors list:
            errors.append("All fields are required.")

        #--------------------------------------#
        #-------- VALIDATE MIN LENGTHS: -------#
        #--------------------------------------#
        # If all fields are not at least 2 characters:
        for key, value in kwargs.items():
            if len(value) < 2:
                # Add error to errors list:
                errors.append(key + " field must be greater than 2 characters.")

        #--------------------------------------#
        #----------- RETURN ERRORS: -----------#
        #--------------------------------------#
        # return list of errors:
        return errors


    def create_book(self, **kwargs):
        """
        Sends book for validation and either creates new book or returns errors.

        Parameters:
        -`self` - Instance to whom this method belongs.
        -`**kwargs` - A dictionary of book data accompanied by two asterisks (mandatory)
        """

        # Validate form:
        validation_errors = self.__validate(**kwargs) # This will be a list of errors (possibly empty if none).
        # The above variable creation runs our private function defined above, `__validate()`, passing along form info as `**kwargs`.

        # If validation errors, send back errors without book creation:
        if len(validation_errors) > 0:
            print validation_errors
            # Send errors list back:
            return {
                "errors": validation_errors
            }
        # If validation passes, create new book:
        else:
            print "Validation passed."
            print "Creating new book..."
            # Create new book with data submitted:
            new_book = Book(title=kwargs['title'], category=kwargs['category'], author=kwargs['author'])
            # Save new book (mandatory or DB won't update):
            new_book.save()
            # Return new book:
            return new_book


class Book(models.Model):
    """
    Creates instances of a `Book`.

    Parameters:
    -`models.Model` - Django's `models.Model` method allows us to create new models.
    """

    title = models.CharField(max_length=50) # CharField is field type for characters
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) # DateTimeField is field type for date and time
    updated_at = models.DateTimeField(auto_now=True) # note the `auto_now=True` parameter
    objects = BookManager() # Attaches `BookManager` methods to our `Book.objects` object.
