# Optional Assignment: Books and Authors

Build on your previous assignment. Make a new table for authors with the assumption that each book can have only one author. How will your book table change? Be sure you can add a book and an author and the relationship between them.

## To Do:

1. Create your new database model and make any needed changes to your Book model.

2. Migrate!

3. Open shell.

4. Create 5 new books.

5. Create 5 new authors.

6. Assign author #1 to the first 2 books.

7. Assign author #4 to the rest of the books.




## Where I left Off / Developmental Bugs:

- When I first built my model, to establish my one-to-many relationship, I set
the `foreignKey` in my `Book` model to an `Author` object. Unfortunately, I at first
thought I could set just the `id` (and I am sure that I can, but have not figured out how yet).
Essentially, I named this field at first `author_id`, however with my `ForeignKey` setup,
it only allowed for instances of an `Author`, not a discrete integer. Alas, I set the field
then to my `Author` object, and instead, to access the author's `id`, I must reference it as such:
`author_id.id`. I tried to change my property of my table back to `author` instead of `author_id`,
so that I could simply grab the `id` via `author.id`. Unfortunately, these changes seem not to take.
Trying to `makemigrations` was throwing an error, basically saying it required an `author_id`, although
I'd removed any references to such property. It appeared as though my changes weren't taking, although I
understand it is instead something I'm doing wrong.
