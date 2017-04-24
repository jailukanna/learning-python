students = [ 
     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


# PART 1:
# print each full student name:
for i, entry in enumerate(students):   # iterates over each dictionary, 'i' being index count and 'entry' being <key_name>
	print entry['first_name'], entry['last_name']  # grabs entry 'first_name', 'last_name' - a space is automatically added when separating by commas



# PART 2:
# print the <number of category> - <full name in caps> - <character count for full name>
# example, 1 - MICHAEL JORDAN - 13
users_list = users.items()  # converts users dict to a list stored as 'users_list'
for key, data in users_list:    # for key, data in 'users_list'
	print key 
	for count, value in enumerate(data, start=1):
		print count, "-", value["first_name"].upper(), value["last_name"].upper(), "-", len(value["first_name"]) + len(value["last_name"])
