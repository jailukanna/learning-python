# Assignment: Login and Registration
Rebuild the Login and Registration assignment from the flask chapter, this time using Django.

We’ve learned how to integrate models, validations, and controllers to our projects. Our next goal is to create a fully functional login and registration app! This will combine your knowledge of MVC patterns, validations, and password encryption.


Build the following:
+ Show validation error messages if validations fail the following tests
+ First Name - Required; No fewer than 2 characters; letters only
+ Last Name - Required; No fewer than 2 characters; letters only
+ Email - Required; Valid Format
+ Password - Required; No fewer than 8 characters in length; matches Password Confirmation

Don't worry about hashing passwords for now. We'll take a closer look at hashing tomorrow.

+ Bonus: Birthday Field - Before today, or go creative and do it in an age range
+ Bonus: Implement Flash Messages

### One thing we've noticed as people build their login and registrations that you should consider:

`User.objects.get(email = email)`
- If there is not a matching email for a `.get()`, Django throws an error (try and except could come in handy).
- Otherwise it returns the User object associated with the matching user. e.g. `Userobject`.

`User.objects.filter(email = email)`
- `.filter()`, on the other hand, returns a list, so if there is no user that matches, it returns an empty list.  
- If there is a single matching user the list will contain a single User object: e.g. `[Userobject]`.


## Project Notes / Where I left Off:
    - Can you refactor your validation methods and break them into smaller units at all? Just an idea...
    - Any other way to simplify, streamline or clean up your code?
    - **Experiment with the built in password validators -- see settings.py password validation section**

## Development Issues:
    - *Model.objects.get() method*: One thing that's important to understand is that when you use `User.objects.get()` in Django models, if no item is found,
    you get a `DoesNotExist` error. Unfortunately, you can't simply use this in your exception, ie `try: .... except DoesNotExist:`.
    The `DoesNotExist` will not be recognized. Instead, you must place your Model name in front, ie, `except User.DoesNotExist:` will be recognized!
    http://stackoverflow.com/questions/23464269/django-using-try-and-except

    - *Django Messaging*: In this project I revamped it to take advantage of Django messaging. In many ways, my style was nice and clean,
    however, I wanted to experiment. I don't know if there is a loss in computing efficiency, etc, however I had to pass my entire request
    object in my `views.py` over to my `models.py`, so that I could take advantage of the `messages` Django module. Not only did I have to pass
    my request object along to the `models.py`, but I could not simply redirect to my index route when errors were detected: I had to render
    the index page, as this passes along the updated request object -- and this is where Django stores its error objects. Doing some personal
    error handling, or a homebrew method is likely to be less shuffling around of the request object, but alas, this is taking advantage of
    Django's native features, and probably is "best practices". (But we'll keep learning).

    - *Validation Philosophy/Pseduocode*: In this file, we have a manager running for our Users model. We have created two methods as extensions onto
    our model Manager. The first handles the registration validations. All fields are validated, any errors are generated based upon validations, and
    if errors are detected, the index page is loaded along with the errors and a `None` is returned. If no validation errors occur, the users's password is hashed, and the fully updated user data (as a `dict`) is sent back to views.py to be created. The second method handles the login validation. If any fields are flagged, errors are generated and a `None` is returned. If fields pass validation, `True` is returned. I'd like to break my validations
    into smaller bits for ease of reading, and to make things a bit more logical. I think for the most part it's OK, but it could be a little too busy.
    I think it's important to keep aiming for simplicity and organization. The more simple and organized, the better for everyone. Don't overcomplicate
    and over-busy things (my seeming slanted natural reaction..)
