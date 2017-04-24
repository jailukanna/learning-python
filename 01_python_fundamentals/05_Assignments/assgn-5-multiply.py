def multiply(a,b): # creates new function named 'multiply' with accepted parameters (a,b)
	result = [x * b for x in a]   # creates var and for each position (x) in a, multiply that by b 
	print result

a = [2,4,10,16]  # our list

multiply(a,5) # runs our function with our arguments a, 5