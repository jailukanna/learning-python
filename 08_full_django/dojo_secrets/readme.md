# Assignment: Dojo Secrets
Create a Django app where registered users can post and like secrets.

+ Login and registration system. Validations apply.
+ Users can post secrets, delete secrets that they posted, and like secrets posted by others.
+ On the index page, display the 5 or 10 most recent secrets. Also include a "Most Popular" page, which shows all secrets, sorted by number of likes (most likes is first).
+ On both index and "Most Popular" page, show how many likes the secrets has received, a link to like that secret if the user hasn't already, and--if the logged-in user posted this secret--an option to delete. Also show when the secret was posted.
+ Secrets are anonymous--never display the name or E-mail of the person who posted the secret.

# Personal Additions:
+ Added `session`, so user data is stored on server upon login.
+ Added an authorization check when gathering dashboard data, so if User is not currently in session, then the index page is loaded.

# Where I Left Off:
- Experiencing a weird issue where it seems that popular secrets, if there are only 2, is populating 2 entires twice. Troubleshoot this next, but overall, this baby is locked down.

# Development Notes:
- Issue: "Time since" setup for Secret Timestamps on Template.
    + Solution: Use Django's built in `timesince` attribute when building your Template variables. IE, `{{secret.created_at|timesince}}` will output the time since in comparison with current time.

- Issue: After performing a many-to-many `.add()`, print statement of `secret.likes` was coming up as `secrets.User.None`.
   + Solution: Always call `.all()` after your many-to-many field,
   to see a query of all objects. The correct way to get the Users
   to print is to use `secret.likes.all()`.

# Things To Do:
- Clean up routing and controller methods so everything is clean.
- Can you refactor and clean up the error handling?

## Notes about Black Belt Exam Template:
- Make a detailed list of all variable names that need to be updated if you pulled a repo.
