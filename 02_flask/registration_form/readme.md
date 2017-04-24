# Overview:
This is just a basic Flask (0.12.1) application (no Django) which runs some
basic user validation. This project also utilizes `flash` messaging and
uses categories in order to show error and success messages.

## Notes / Issues Experienced When Building this Project:
+ If using `flash` messaging, you can separate your messages into categories.
+ See: http://flask.pocoo.org/docs/0.10/patterns/flashing/#flashing-with-categories
+ The documentation was a little confusing, but you'll see in `templates/index.html` that you can define a second parameter when setting up your flash messaging, which becomes a category.
+ We can then filter for the catergory when using `get_flashed_messages()` in the View
