a = [1, 2, 5, 10, 255, 3]

# in this method the sum of the list is taken and then divided by the number of items in the list, aka, the len() function
print sum(a) / len(a)


# here's another way but longer using for loops
sum = 0
for num in a:
	sum += num
avg = len(a)
average = sum / avg
print average