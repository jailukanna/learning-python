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



## Project Notes:
    - This would be a great template to build for your PYTHON belt exam.
    - Investigate the differences between your style of creating errors, and the flash-messaging built into Django.
    - It's possible you worked harder than you had to, ie, the flash messaging is probably easier than you think.
    - This project does not include hashing. Build that into your TEMPLATE for this LOGIN/REGISTRATION
    - Refactor wherever possible.
    - Setup Session so it can be easily imported also.
    - **Experiment with the built in password validators -- see settings.py password validation section**

## Development Issues:
    - Note: One thing that's important to understand is that when you use `User.objects.get()` in Django models, if no item is found,
    you get a `DoesNotExist` error. Unfortunately, you can't simply use this in your exception, ie `try: .... except DoesNotExist:`.
    The `DoesNotExist` will not be recognized. Instead, you must place your Model name in front, ie, `except User.DoesNotExist:` will be recognized!
    http://stackoverflow.com/questions/23464269/django-using-try-and-except
