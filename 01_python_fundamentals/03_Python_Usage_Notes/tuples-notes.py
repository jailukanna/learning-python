
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")


# print index value of 2
print julia[2]



# print all results using a for loop
for data in julia:
	print data


# although tuples cannot be changed, we can add and slice tuples
julia = julia + ("Eat Pray Love", 2010)
print julia

# inserts our new tuple data in between index 3 and 5
julia = julia[:3] + ("Movie Name", 2015) + julia[5:]
print julia


# tupple packing

value = ("Michael", "Instructor", "Coding Dojo") # tuple packing
(name, position, company) = value # tuple unpacking
print name
print position
print company



# swapping values
(a, b, c, d) = (1, 2, 3, 4)
(a, b, c, d) = (b, a, c, d) # this actually swaps position
print (a, b, c, d)



# <--- built in tuple functions

# len
tuple_data = ('physics', 'chemistry', 1997, 2000)
print len(tuple_data)




# max and min
tuple_data = ('physics', 'chemistry', 'x-ray', 'python')
tuple_num = (67, 89, 31, 15)

# max
print max(tuple_data) 	# should print the max value of tuple-data (this value will be the string with the first letter whom is furthest down the alphabet)
print max(tuple_num)	# this will print the max int

# min
print min(tuple_data)	# prints string value whose first letter is closest to first letter in the alphabet	
print min(tuple_num)	# prints min int value


# sum
tuple_num = (67,89,31,15)
print sum(tuple_num) # adds all values in the tuple

# any
# returns True if *any* value in tuple is True (ie, integer, string, list, etc)
# returns False if *any* value in tuple is Fale (ie, '0', empty list [], or empty string '')
tuple_num = (67, 89, 31, False, 0, None)
print all(tuple_num) # because '0', 'False', and 'None' exist in our tuple, this value returns false


# all
# returns True if *all* items are True, returns False if *all* items are False
tuple_num = (67, 89, 31, False, 0,  None)
print all(tuple_num)


# enumerate
# enumerates through the tuple and returns a tuple with 2 values (index, item). Gives us back the index and each element in the original sequence.
num = (1, 5, 7, 3, 8)
for index, item in enumerate(num):
	print(str(index) + " = " + str(item))


# sorted
# iterate through a tuple and sorts it and returns it in order - note that the returned item is a *list* not a tuple
num = (1, 5, 7, 3, 8)
print sorted(num)


# reversed
# sort through a tuple and reverse the order - note that the returned item is a *generic object* and must be fed into a tuple() or list()
num = (9, 1, 8, 2, 7, 3)
print tuple(reversed(num))



# tuple as return values
# we can use tuples in functions to return multiple values
def get_circle_area(r):
	# returns (circumference, area) of a circle of radius r
	c = 2 * math.pi * r
	a = math.pi * r * r
	return (c, a)  # by using parentheses, our variables are returned in the form of a tuple
