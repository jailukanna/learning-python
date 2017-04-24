# python's testing framework is included in the standard python library.
# let's create a simple unit below and test it:


# import the python testing framework
import unittest
# our "unit"
#this is what we're running our test on:

def isEven(n):
	return n % 2 == 0

# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase (unittest.TestCase gives us access to a whole bunch
# of different methods that we can use to write our tests:
class IsEvenTests(unittest.TestCase):
	# each method in this class is a test to be run:
	def testTwo(self):
		self.failUnless(isEven(2))
	def testThree(self):
		self.failIf(isEven(3))

# if __name__ == '__main__':
# 	unittest.main() 

	# this runs our tests
	# By including these two lines, we can run our test code by executing our python file. 
	# Running it with no options results in a simple output but running this file with the '-v' flag will 
	# give you the verbose output with information on each test that was run

# the general TDD flowis:
# think of feature -> write tests -> run and fail -> code -> run and pass -> refactor -> repeat

# most of our test cases are looking to assert the TRUTH of a condition, which we will then use: assertTrue()
# if we want to test for a produced FALSE value, we instead can use assertFalse()

class TruthTest(unittest.TestCase):
	def test_assert_true(self):
		my_value = True
		self.assertTrue(my_value)
	def test_assert_false(self):
		my_value = False
		self.assertFalse(my_value)

if __name__ == "__main__":
	unittest.main()