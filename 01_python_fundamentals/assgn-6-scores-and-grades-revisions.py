print "Welcome to my program! Please enter your scores to see the grade."
scores = []  # this creates an empty list that we'll use to store our user inputs (scores)
count = 1  # this initializes a count variable at 1 for the while loop to come
while count <= 10: # this goes through the while loop 10 times
	scoreInput = raw_input("Please enter a score between 60 and 100: ") # asks user for score
	scores.append(scoreInput) # appends this score to our scores list
	count = count + 1 # increases the count variable by 1
print "Scores and Grades"
for elem in scores: # this for loop assesses each element (each user input) in our list and
	x = int(elem) # takes each user input and turns it to an integer and stores it as x
	if x >= 90:	# evals x for 90+ is an A
		grade = 'A' 
	elif x < 90 and x >= 80: # evals x for 80-89 is B
		grade = 'B'
	if x < 80 and x >= 70: # evals x for 70-79 is C
		grade = 'C'
	elif x < 70 and x >= 60: # evals x for 60-69 is D
		grade = 'D'
	if x < 60: # evals x for 59 and below is F
		grade = 'F'
	print "Score: {}; Your grade is {}".format(elem, grade) # prints each element and the corresponding grade

print "End of program. Goodbye!" # tells user to end program (note this is outside of our for loop)



# Here's another way to run this program:

print "Scores and Grades"
for count in range(0, 10):
	score = input("Please enter your score:")

	if(score <= 70):
		grade = "D"
	elif(score <= 80):
		grade = "C"
	elif(score <= 90):
		grade = "B"
	else:
		grade = "A"

	print "Score: %d; Your grade is %s" %(score, grade)  # notice the use of the variables here

print "End of program. Bye!"