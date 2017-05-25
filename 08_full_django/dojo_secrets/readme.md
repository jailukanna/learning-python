# Assignment: Dojo Secrets
Create a Django app where registered users can post and like secrets.

+ Login and registration system. Validations apply.
+ Users can post secrets, delete secrets that they posted, and like secrets posted by others.
+ On the index page, display the 5 or 10 most recent secrets. Also include a "Most Popular" page, which shows all secrets, sorted by number of likes (most likes is first).
+ On both index and "Most Popular" page, show how many likes the secrets has received, a link to like that secret if the user hasn't already, and--if the logged-in user posted this secret--an option to delete. Also show when the secret was posted.
+ Secrets are anonymous--never display the name or E-mail of the person who posted the secret.




# Development Notes:
- Add Security Check so /dashboard cannot be accessed otherwise.
- Clean up routing and controller methods so everything is clean.
- Can you refactor and clean up the error handling?

# Notes about Black Belt Exam Template:
- Make a detailed list of all variable names that need to be updated if you pulled a repo.


# Where I Left Off:
- Got the data I mostly need for template. But right now am building the dictionary
in the new secret function and using the dashboard.py helper functions. However,
this is too busy. Just boil it down to one function that grabs everything you need
and hands back a full fledged dict. You can then just pass this to your Template
without any extra work or code in your views.py (like you're doing now, generating
the entire dictionary).

- Setup security so the dashboard page cannot be accessed unless a valid session.
