# Assignment: Books
Create a new Django project and add a books model. Complete the below functionality.

1. Create Books model
Your model should contain the following fields: title, author, published date, category.

2. Migrate
Make your migrations and activate shell.

3. Create and show Books
Make 5 new books and retrieve them all, as before.

4. Add a new field
Add a field to your table called in_print. This should be a boolean field.

What should you do to see your changes reflected in your database table? You'll have to `makemigrations` and `migrate` again. Once you do, a prompt will walk you through filling in values for the existing entries. Why is this? Discuss with your cohort-mates. Ask an instructor if you and your friends can't work it out.



### Where I left Off:
+ For some reason when i try and add a field to my model, it won't let me run migrations, saying the column doesn't exist.
Why is this happening?

Here's the output:
django.db.utils.OperationalError: table books_book has no column named in_print


(when trying to add `in_print` to `Book`)
