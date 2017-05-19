# Assignment: Login and Registration

**Note**
This file is 1 of 2 projects which achieve the same functionality. V2 handles error generation differently when it comes to validations, and thus is contained in its own project.
This project takes the approach of generating django-messages errors within the models.py file, but could potentially be hazardous to spoofed routes, as the entire request object
is passed to models.py. I don't know how absolutely weak or strong this method is, so I am saving 2 versions of this project, one which passes the entire request object, another which
does not, and am going to later try and hack/break them and see what goes down.

See `login_registration_2` for the version of this project where the request object is more protected.

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

    - *Validation Philosophy/Pseduocode*: For now, what happens is the validators receive a request object, and then extract the data they
    need for validations. If validations are passed, the new user is either created and returned, or the user is retrieved from the DB and returned.
    If the user fails validations, `False` is returned.

    - *Notes About Validations & Django Messages*: Essentially, the way you've got things setup right now, is that you're sending the entire `request` object
    over to your django models.py. The only issue with this, if someone spoofed your routes and tried to send false data, the request object could reach
    your models.py. This could then be used to initiate commands to your DB or corrupt data, etc. It was advised to not pass the entire `request` object, as
    this opens the django application up to some potential liabilities. The only issue that should be noted is perhaps if you more iron lock down some of the
    validations in `models.py`, for example, if you check for explicit keys in the request object.

    Because of this potential `request` issue, I am going to duplicate this entire project into a new project called `logreg2`, and will be in the primary project:
    `login_registration_2`.
