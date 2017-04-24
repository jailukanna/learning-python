# helpful notes for this project - use pytho random module to generate a random number
# import random
# random_num = random.random()
# # the random function will return a floating point number,
# # that is 0.0 <= random_num < 1.0
# 2. Use the python built-in round function to convert that floating point number into an integer

# see example below how to now round a decimal number
# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# y_rounded will be rounded up to 1

import random

def randomNumber():
	x = random.random()
	x_rounded = round(x)
	return x_rounded

head = 0
tail = 0
for count in range(1, 50001):
	z = randomNumber()
	if z == 1.0:
		coin = 'Head'
		head = head + 1
	else: 
		coin = 'Tail'
		tail = tail + 1
	# print "Attempt #%s: Throwing a coin...it's a %d! ... Got %s head(s) so far and %d tail(s) so far!" %(count, coin, head, tail)
	print "Attempt #%d: Throwing a coin... It's a %s! ...Got %d head(s) so far and %d tail(s) so far!" %(count, coin, head, tail)
print "Ending the program, thank you!"





# see this alternative method

import random
import math

print 'Starting the program'

head_count = 0
tail_count = 0
for i in range(1,5001):
    rand = round(random.random())    # notice in this example how the random function is called and rounded all in one line -- great line of code
    if rand == 0:
        face = 'tail'
        tail_count += 1
    else:
        face = 'head'
        head_count += 1
    print "Attempt #"+str(i)+": Throwing a coin...It's a "+face+"!...Got "+str(head_count)+" head(s) and "+str(tail_count)+" tail(s) so far"

print 'Ending the program, thank you!'
