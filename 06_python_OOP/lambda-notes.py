############
#
#	Lambda (Anonymous) Functions
#
############
'''
	+ used when we only need to use a function once
	+ lightweight
	+ convenient if we need to provide a function as a paramter to another function
'''

def square(num):
	x = num ** 2
	return x

# here's how we can rewrite this as a lambda function

adder = lambda num: num ** 2   # no return statement

# notice how lambda does not contain a return statement
# they automatically return

# lambdas are expressions, not statements
# expressions are things like strings, numbers or a class instance (object)

# these are all examples of expressions

99
'hello'
[11, 'cat', ('a', 'tuple', 'is', 'me')]
2 + 5
'hello' + 'world'
True
False
lambda x: x + 2

# because the lambda is not a statement, we can use it in places where we would use an expression


# statements are things like:
# variable assignment
x = 35
# if statements
if hungry == True:
	pass
# for loops
for x in (range(10)):
	pass
# while loops
while True:
	break
	# break statements also


# here's how we can use lambdas where def's are not allowed:

# an element in a list using lambda

my_list = ['test_string', 99, lambda x : x ** 2]
# access the value in the list
print my_list[2] # this will print lambda object in memory
# invoke 
my_list[2](5)

# pass lambda to another function as a callback
# define function here
def invoker(callback):
	#invoke the input and pass an argument of '2'
	print callback(2)
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)

# stored in a variable
add10 = lambda x: x + 10
add10(2) # returns 12
add10(98) # returns 108

# returned by another function
def incrementor(num):
	start = num
	return lambda x: num + x


# here's an example of a function that we'll rewrite a lambda in its place
my_arr = [1,2,3,4,5]
def square(num):
	return num ** 2
map(square, my_arr)
# [1,4,9,16,25] is output

# here's how we can use a lambda in place of this function, square() since we only use it once
my_arr = [1,2,3,4,5]
map(lambda x: x ** 2, my_arr)
# map takes two paramenters (1) a function and (2) a list
# because we neer use square() again, instead we can put a lambda expression in its place
# map() now runs the lambda function for each value in the my_arr array
# the output would be [1,4,9,16,25]

'''
these functions also might be good to use a lambda for:

	map()
	reduce()
	sort() - lambda is optional
	filter()

'''









