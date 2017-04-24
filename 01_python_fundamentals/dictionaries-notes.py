# a dictionary is another container type and can store pyton objects, including other containers (tuples, lists)
# dictionaries consist of pairs (called items) of keys and their corresponding values
# dictionaries are also known as, "associative arrays" or "hash tables"

# here are some general characteristics of python dictionaries
	# a dictionary is an unordered collection of objects
	# values are accessed using a key
	# dictionaries can shrink or grow as needed
	# their contents *can* be modified
	# dictionaries can be nested
	# sequence operations such as slice *cannot* be used in dictionaries

# here's a few ways we can create a dictionary:

# literal notation - here we straight up define each value
weekend = { "Sun": "Sunday", "Mon": "Monday" }


# dict() function will create our dictionary using 'one','two' as keys and '1','2' as values
vals = dict(one=1, two=2) 


# creates an empty dictionary that we can add values to
capitals = {} 
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"


# dictionary comprehension - this creates a dictionary with 4 pairs, where the keys are 0,1,2,3 and the values are simple objects
d = { i: object() for i in range(4) }


# note that *each key in a dictionary must be unique*


# accessing dictionary values

print weekend["Sun"]  # prints 'Sunday' from dict above
print capitals["svk"] # prints 'Bratislava' from dict above


# here's a way to use the for loop to access values

# to print all keys
for data in capitals:
	print data

# another way to print all keys
for key in capitals.iterkeys(): # iterates all keys
	print key

# here's a way to print values
for val in capitals.itervalues():
	print val

# to print keys and values
for key,data in capitals.items():
	print key, " = ", data


# built in functions for dictionaries are numerable!

# cmp(dict1, dict2) - compares elements in both dictionaries
dict1 = { "Number": 1, "Date": "8/01", "Week": 3, "Time": "Evening" }
dict2 = { "Number": 2, "Date": "8/02", "Week": 3, "Time": "Morning" }
print cmp(dict1, dict2)


# len() gives length of dictionary
print len(dict1)


# str() produces a printable string representation of dictionary
print str(dict2)


# type() returns the type of the passed variable.
print type(dict1["Number"])
# another example to check type and do something:
if type(dict1["Number"]) == int:
	print "yup"



# here are some dictionary methods
# note that they can be written in two diffent ways
# the first:
#	dict.method(yourDictionary)
# or:
#	yourDictionary.method()
# both will work


# .clear() - removes elements from a dictionary
my_dict = {"Val": 1, "2nd-Val": 2, "3rd-Val": 3}
my_dict.clear()
print my_dict # it will be empty


# .copy() - returns a shallow copy dictionary
dict3 = dict2.copy() # have to define a var first using this function to give it a place to live
print dict3  # now a new copy of our dict2


# .fromkeys(sequence, [value]) - create a new dict with keys from sequence and values set to value
dict4 = dict3.fromkeys("Number", 1)  # not sure what's going on here but gave it a try
print dict4 # QUESTION FOR TA: What's going on here?


# .get(key, default=None) - for key, return value or default if key not in dictionary
print dict3.get("Date")


# .has_key(key) - returns true if a given key is avail. in the dictionary, otherwise returns false
print dict3.has_key("Foods") # this will return false, as this key does not exist


# .items()
# returns a list of dictionary's tuple pairs (key and value)
print dict3.items()


# .keys() - return a list of dictionary keys
print dict3.keys()

# .setdefault(key, default=None) - similar to get() but sets dict[key]=default if key not in dict
print dict3.setdefault("Date", "default=None")


# .update(dict2) = adds dictionary dict2's key-value pairs to an existing dictionary
myNewDictionary = {}
myNewDictionary.update(dict2)
print myNewDictionary


# .values() returns the values of a dictionary - note this is returned as a *tuple*
print myNewDictionary.values()




# Nesting is also allowed in dictionaries. Dictionaries may contain lists and tuples.
context = {
  'questions': [   # opening bracket
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]  # closing bracket
 }

# iterate the values with a nested for loop
for key, data in context.items():
	for value in data:
		print "Question #", value["id"], ": ", value["content"]
		print "----"





# lists from dictionaries
# It's possible to create lists from dictionaries by using the methods items(), keys() and values(). As the name implies the method keys() creates a list, which consists solely of the keys of the dictionary. While values() produces a list consisting of the values. items() can be used to create a list consisting of 2-tuples of (key, value)-pairs:

data ={"house":"Haus","cat":"Katze","red":"rot"}

print data.items()
#[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]

print data.keys()
#['house', 'red', 'cat']

print data.values()
#['Haus', 'rot', 'Katze']



# dictionaries from lists
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

# .zip() function can combine these as a zipper
# Note that if the number of keys and values between lists are different, the extras will be dropped off and ignored
country_specialities = zip(countries, dishes)
print country_specialities

# note that this is only in a tuple form, and we have to create an actual dictionary
country_specialities_dict = dict(country_specialities)
print country_specialities_dict



