# Assignment: Login and Registration V2: Operation Protect the Request
In this assignment we'll do the same thing we did in `login_and_registration`, except we'll be
better protecting our request object when creating django error messages. Please see the bottom
of this log under `Development Issues`, as well as the notes in `index.html`, as well as the notes
at the bottom of `login_registration/readme.md` (project v1) to understand this issue more.


Build the following:
+ Show validation error messages if validations fail the following tests
+ First Name - Required; No fewer than 2 characters; letters only
+ Last Name - Required; No fewer than 2 characters; letters only
+ Email - Required; Valid Format
+ Password - Required; No fewer than 8 characters in length; matches Password Confirmation

## Project Notes / Where I left Off:
    - Can you refactor your validation methods and break them into smaller units at all? Just an idea...
    - Any other way to simplify, streamline or clean up your code?
    - **Experiment with the built in password validators -- see settings.py password validation section**

## Development Issues:
    - *Validation Philosophy/Django Messages*: In this project, a security issue was attempted to be resolved by better protecting
    the request object when performing validations in models.py. Instead of sending the entire request object over to models.py,
    instead a list of errors is returned, and iterated over, and generates our django errors this way. This prevents us from passing
    the entire request object over.
