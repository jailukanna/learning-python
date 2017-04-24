# we can actually use inheritance a different way as well, let's investigate
# the example below


class Other(object):
	def override(self):
		print "OTHER override()"
	def implicit(self):
		print 'OTHER implicit()'
	def altered(self):
		print 'OTHER altered()'

# notice that when we create a child class below,
# that we don't pass along the Other object as a parameter

class Child(object):
	def __init__(self):
		# we will now create an instance of the Other class as an ATTRIBUTE for our Child class
		self.other = Other()

	def implicit(self):
		# we can now tap into the Other() behavior in our child:
		self.other.implicit() # will print 'OTHER implicit'

	def override(self):
		print 'CHILD override()'

	def altered(self):
		print 'CHILD BEFORE OTHER altered()'
		# call a method from our Other() function again:
		self.other.altered()
		print 'CHILD, AFTER OTHER altered()'

son = Child()
son.implicit() # prints 'OTHER implicit()'
son.override() # prints 'CHILD override()'
son.altered()  # prints 'CHILD BEFORE OTHER altered()', 'OTHER altered()', 'CHILD, AFTER OTHER altered()'
# notice that the Other.altered still prints due to line 31

'''
QUESTIONS:
	
	When should we use inheritance vs composition?

		The answer is subjective but here's a few guidelines:

		+ Avoid multiple inheritances at all costs, as it is too complex to be reliable. If you're stuck with it, be prepared to know the class hierarchy and spend time finding how everything descends from parent classes. 
		+ Use composition to package code into modules that are used in numerous unrelated places and situations.
		+ Use inheritance lightly, when there are clearly related reusable pieces of code that fit on a single common concept, or if you must because of something you're using.


'''
