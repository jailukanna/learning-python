a = [1, 2, 5, 10, 255, 3]
print sum(a)


# here's another way to deal with that array:

sum = 0		# creates a sum variable
for num in a:   # this means for each number in the array of a
	sum += num 		# this means add the num to the existing sum value

print sum