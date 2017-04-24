for count in range (1, 2001):
	if count % 2 == 0:	# if statement examines if modulus % 2 is 0 (even), and if so:
		oddOrEven = 'even'	# updates a new variable as a string, 'even' (note, we didn't have to define this var first)
	else:  # else if % 2 is not 0 (which means it is odd) then:
		oddOrEven = 'odd' # set our variable as a string to 'odd'
	print "Number is {}. This is an {} number.".format(count, oddOrEven)  # print the string with our new variables



# here's another way to do it from the solutions sheet

for i in range (1,2001): # goes through the *range* of 1 -> 2001
	if i % 2 == 0: # if modulus 2 is 0 (odd) then:
		print 'Number is ' + str(i) + '. This is an odd number.' # print the integer as a string and state odd
	else: 
		print 'Number is ' + str(i) + '. This is an even number.' # otherwise print integer and state as even