# Django Shell

In this assignment, you will learn how to interact with the Django Shell (similiar to Mongo shell), which will allow you to interact with your SQLite DB (or any DB you've assigned to your project).

To access the Django Shell, we must first have an app created in our Django Project, and have also defined our models in `models.py`. 

Follow the instructions below:

1. Start a project according to the procedure you learned in the Django intro section
2. In models.py create a class that corresponds with a table
3. Give the new class attributes that represent columns in a table
4. Run Migrations (in Terminal):
	`makemigrations`
	`migrate`

5. Now what??

Instead of building out our app to run and serve data, we can simply stop here and open Django shell to interact with our models. We'll be using the shell to experiment with writing queries using Django's ORM. Django shell is a lot like the Python shell. You'll use your project's manage.py to enter a command-line interface that allows you access to your project's files and the database connected to it.

In terminal, from your project's root directory, enter the following:

	`python manage.py shell`

Your terminal output should look like so:

	* See `./shell.png` *

Once you're in shell, you'll have access to the functions contained in your files. However, just like in your Python documents, you have to import the modules (files) that you need. Note: be sure to replace anything with {{}}, including the braces with the correct project and app names for your project. Enter the following with the appropriate values replaced.

	`from apps.{{app_name}}.models import {{table_name}}`

Now we'll learn two ORM queries that will help us insert into and read from the database. We'll use the course example from the previous tab.
	
	`course = Course.objects.create(name="Python",description="Learn how to write Python like a boss.")
	course
	# your result will look like:
	# <Course: Course object>`

Now how can we look at what's in that Course object? We can call out individual attributes. Try: course.name. Your output should be: 'Python'

Now we can get all the items from the table:

	`courses = Course.objects.all()
	courses
	# your output will be:
	# <QuerySet [<Course: Course object>]>`

NOW how do we view our data?

`for course in courses:
	print course.name, course.description

	# output should be:
	# Python Learn how to write Python like a boss.`

Now we can insert a row and view all of the entries in that table. We'll try this a few times before we start running more complex queries. Add another row to your course table. Now what do you see when you get all courses and loop through them?
