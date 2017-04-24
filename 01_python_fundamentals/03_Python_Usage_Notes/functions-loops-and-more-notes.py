

# for loops
# for count in range (0, 10):
# 	print "for looping -- ", count






# loop through a list and print element
my_list = [1,2,3,4,5]
for element in my_list:
	print element






# while loops are good to go through code until a condition is met -- good for when you don't know how many times you need to iterate
# for count in range(0, 5):
# 	print "while looping -- ", count


# here's another way to write it
# count = 0
# while count < 5:
# 	print 'looping --> ', count
# 	count += 1





# break statement exits a loop - in this example our loop breaks
# for val in "string":
# 	if val == "i":
# 		break
# 	print(val)






# continue statement returns to beginning of loop - the continue statment rejects or skils the remaining statements in the current iteration and goes back to the top - in this example the string will continue to print
# for val in "string":
# 	if val == "i":
# 		continue
# 	print(val)







# pass statement - this is a null operation and will basically do nothing. This may be useful if you are trying to build out features but want nothing to happen with them for now

# class EmptyClass:
# 	pass

# for val in my_string:
# 	pass








# else statement
# x = 3
# y = x
# while y > 0:
#   print y
#   y = y - 1
# else:
#   print "Final else statement"










# Functions

# def add(a,b):		# this defines our new function accepting 'a,b' as parameters
# 	x = a + b 		# this then says how to process a and b
# 	return x		# and tells us to return x (when we return we also store)

# print add(3,5)		# this then calls our function with our arguments


# def hi(name):
# 	print "Hi there, " + name

# hi('tim') 		# calls my new function with my new name
# hi('margot')


# # note that the parameter is 'name' from the above example, while the argument in the function is 'tim' or 'margot' respectively. Parameter and arguments are not the same thing


# def add(a, b):  # must use the def word to define the new function
#   x = a + b
#   return x
# sum1 = add(4,6)  # returns 10 to store as sum1
# sum2 = add(1,4)	 # returns 5 to store as sum2
# sum3 = sum1 + sum2 		# returns 15 as sum3







# Using Variables
	# print "Number is {}. This is an {} number.".format(count, oddOrEven)  # print the string with our new variables





# using raw_input:
	# variableName = raw_input("Please enter your raw input: ")



# check if a list item is a string (or int if you change variable)
	# for elem in arr:
		# if isinstance (elem, str) == True:  # checks if elem is a str


# turns all string characters to lower
	# print elem.lower()

# print only the first letter in a string:
	# print elem[:1].lower()

# how to create a random number and then round it

	# import random

	# def randomNumber():
	# 	x = random.random()  # note that a decimal number is generated
	# 	x_rounded = round(x)
	# 	return x_rounded



