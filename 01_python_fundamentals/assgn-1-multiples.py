# # Mulitples Part 1

for count in range (1, 1000):
	if count % 2 == 1:
		print count



# Multiples Part 2
# - create a program that lists numbers 5 - 1,000,000 in groups of 5
# - below we see the format range(<start-number>, <max number>, <desired mulitple or grouping>)
# - we use print to print and list to print the list of conditions in the range

print(list(range(5, 1000005, 5)))


# here's another way you could write it using for loops instead of the line above (which is a decent method)

for i in range(5, 1000001):   # a for loop goes through numbers 5 - 1,000,000
	if(i % 5 == 0): 		 # if i / 5 has a remainder of 0 (remember modulus)
		print i 			# print i