############
#
#	_.Underscore Assignment (build a custom method library using lambda functions)
#		Tim Knab - Coding Dojo - September 2016
#
#	Updated: 4/28/17
#
############
"""
See: http://underscorejs.org for explanations of each method. This is a Python
library designed to mimick the JS library, but to a much lesser level of detail,
and more so is a practice for usage of `lambda` functions, which we utilize
here as callback methods.

Notes: When invoking the methods below, whatever function is given as the lambda,
will fulfill the `function` parameter within each method. Therefor our library
simply applies whatever function is given as lambda to whatever logic we set forth
in our methods below. This allows us flexibility and is pretty cool.
"""


class Underscore(object):

	def map(self, myList, function):
		"""Runs each value in a list through a function.

		Parameters:
		--myList: List of values (integers).
		--function: This is the callback function that runs (lambda) based on List values.
		"""
		newList = []
		for x in range(len(myList)):
			# Note: When this runs, the `function` parameter will be fed a `lambda` function,
			# which works like a callback function. Whatever function we define as our `lambda`
			# will be applied to this list based upon the following algorithm. This proccess
			# is the same for all other usages of `function` in this document.
			newList.append(function(myList[x]))
		return newList

	def reduce(self, myList, function):
		"""Boils down a list to a single value.

		Parameters:
		--myList: List of values to boil down.
		--function:: How list should be manipulated (lambda callback function)
		"""
		value = 0
		for x in range(len(myList)):
			value += function(myList[x])
		return value

	def find(self, myList, function):
		"""Look through each value in a list for which one passes a truth test."""

		value = 0
		for x in range(len(myList)):
			if function(myList[x]):
				value = myList[x]
				break
		return value

	def filter(self, myList, function):
		"""Look through each value in a list and return an array for values whom pass truth test."""

		newList = []
		for x in range(len(myList)):
			if function(myList[x]):
				newList.append(myList[x])
		return newList

	def reject(self, myList, function):
		"""Look through a list and return only elements that did not pass the truth test."""

		newList = []
		for x in range(len(myList)):
			if not function(myList[x]):
				newList.append(myList[x])
		return newList


# Instantiate our above `Underscore` class:
_ = Underscore()

# Test our `_` library functions:
evens = _.filter([1,2,3,4,5,6], lambda x : x % 2 == 0)
print evens
# prints [2, 4, 6]

mappings = _.map([1,2,3], lambda x : x * 3)
print mappings
# prints [3, 6, 9]

reducing = _.reduce([1,2,3], lambda x: x )
print reducing
# prints 6

finding = _.find([1,2,3,4,5,6], lambda x: x % 2 == 0)
print finding
# prints 2

filtering = _.filter([1,2,4,8], lambda x: x > 2)
print filtering
# prints [4, 8]

rejecting = _.reject([1,2,4,8], lambda x: x > 2)
print rejecting
# prints [1, 2]
