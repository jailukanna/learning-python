ifrom django.shortcuts import render, HttpResponse

# this will grab our Users table from our models.py
from .models import Users


# Create your views here.
def index(request):
# prints table name, prints current objects, creates a new object then prints again:
	print User._meta.db_table # this should print table name in case you ever forget
	print Users.objects.all() # this sould print every object in the Users table
	Users.objects.create(first_name='Tim', last_name='Knab', pw_hash='123123123') # creates a user object, Tim Knab with a pw hash of 123123123
	print Users.objects.all() # your new user should now appear
	
# retrieves object, prints first_name of object, sets first_name of object, saves, gets again and prints:
	u = Users.objects.get(id=1) # gets object with id of 1
	print u.first_name # should print first_name (dot notation)
	print u['first_name'] # should print first_name (bracket notation)
	u.first_name = 'Timothy' # sets first name to Timothy (was formerly Tim)
	u.save() # saves this change to the object
	j = Users.objects.get(id=1) # create a new variable and have it retrieve object with id of 1
	print j.first_name # gets user with id of 1 (should now be Timothy)

# retrieve object using first_name instead of id, use raw mysql, print all users with a for loop:
	print Users.objects.get(first_name='Timothy') # gets user object with first_name of Timothy
	users = Users.objects.raw("SELECT * FROM wall_users") # use of .raw() to use SQL commands directly (instead of ORM)
	# for 'wall_users', django format must be: app_name+_+lowercase_model_name
	# so, for the case of 'Users' and app 'Wall', it's 'wall_users'

	for user in users:
		print user.first_name

	return HttpResponse('OK')

