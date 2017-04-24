############
#
#	_.Underscore Assignment (build a custom method library using lambda functions)
#		Tim Knab - Coding Dojo - September 2016
#
############

class Underscore(object):

	def map(self, myList, function):
		newList = []
		for x in range(len(myList)):
			newList.append(function(myList[x]))
		return newList

	def reduce(self, myList, function):
		value = 0
		for x in range(len(myList)):
			value += function(myList[x])
		return value

	def find(self, myList, function):
		value = 0
		for x in range(len(myList)):
			if function(myList[x]):
				value = myList[x]
				print value
				break
		return value

	def filter(self, myList, function):
		newList = []
		for x in range(len(myList)):
			if function(myList[x]):
				newList.append(myList[x])
		return newList

	def reject(self, myList, function):
		newList = []
		for x in range(len(myList)):
			if not function(myList[x]):
				newList.append(myList[x])
		return newList


_ = Underscore()
evens = _.filter([1,2,3,4,5,6], lambda x : x % 2 == 0)
print evens

finds = _.map([1,2,3], lambda x : x * 3)
print finds

mappings = _.reduce([1,2,3], lambda x: x )
print mappings

reducing = _.find([1,2,3,4,5,6], lambda x: x % 2 == 0)
print reducing

rejecting = _.reject([1,2,3,4,5,6], lambda x: x % 2 == 0)
print rejecting