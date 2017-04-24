##########
#
#	MathDojo Assignment - Tim Knab - Sept 2016
#
##########

'''
	///////////////
	// QUESTIONS //
	///////////////

		# QUESTION 1: Any idea why my result() method gives me this error?
			`TypeError: 'int' object is not callable`

		# QUESTION 2: Is there any way I could refactor this code?

'''

class MathDojo(object):
	def __init__(self, result=0):
		self.result = 0

	def add(self, n, *restOfArg):
		# check if first value is a list
		if type(n) == list:
			# go through the list
			for index in range(len(n)):
				# check if int
				if type(n[index]) == int:
					self.result += n[index]
				# check if list
				if type(n[index]) == list:
					# go through list
					for listIndex in range(len(n[index])):
						self.result += n[index][listIndex]
				# check if tuple
				if type(n[index]) == tuple:
					# go through tuple
					for tupleIndex in range(len(n[index])):
						self.result += n[index][tupleIndex]

		# if first value is an integer
		if type(n) == int:
			self.result += n

		# if first value is a tuple
		if type(n) == tuple:
			# go through list
			for index in range(len(n)):
				# check if int
				if type(n[index]) == int:
					self.result += n[index]
				# check if list
				if type(n[index]) == list:
					# go through list
					for listIndex in range(len(n[index])):
						self.result += n[index][listIndex]
				# check if tuple
				if type(n[index]) == tuple:
					# go through tuple
					for tupleIndex in range(len(n[index])):
						self.result += n[index][tupleIndex]

		# if restOfArg is provided
		if restOfArg is not None:
			# run through the restOfArg tuple values
			for index in range(len(restOfArg)):

				# check if list
				if type(restOfArg[index]) == list:
					# run through the list
					for listIndex in range(len(restOfArg[index])):
						# if int
						if type(restOfArg[index][listIndex]) == int:
							self.result += restOfArg[index][listIndex]
						# if list
						if type(restOfArg[index][listIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][listIndex])):
								self.result += restOfArg[index][listIndex][nestedListIndex]
						# if tuple
						if type(restOfArg[index][listIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][listIndex])):
								self.result += restOfArg[index][listIndex][nestedTupleIndex]


				# check if integer
				if type(restOfArg[index]) == int:
					self.result += restOfArg[index]

				# check if tuple
				if type(restOfArg[index]) == tuple:
					# run through the tuple
					for tupleIndex in range(len(restOfArg[index])):
						# if int
						if type(restOfArg[index][tupleIndex]) == int:
							self.result += restOfArg[index][tupleIndex]
						# if list
						if type(restOfArg[index][tupleIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][tupleIndex])):
								self.result += restOfArg[index][tupleIndex][nestedListIndex]
						# if tuple
						if type(restOfArg[index][tupleIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][tupleIndex])):
								self.result += restOfArg[index][tupleIndex][nestedTupleIndex]
		# return
		return self

	def subtract(self, n, *restOfArg):
		# check if first value is a list
		if type(n) == list:
			# go through the list
			for index in range(len(n)):
				# check if int
				if type(n[index]) == int:
					self.result -= n[index]
				# check if list
				if type(n[index]) == list:
					# go through list
					for listIndex in range(len(n[index])):
						self.result -= n[index][listIndex]
				# check if tuple
				if type(n[index]) == tuple:
					# go through tuple
					for tupleIndex in range(len(n[index])):
						self.result -= n[index][tupleIndex]

		# if first value is an integer
		if type(n) == int:
			self.result -= n

		# if first value is a tuple
		if type(n) == tuple:
			# go through list
			for index in range(len(n)):
				# check if int
				if type(n[index]) == int:
					self.result -= n[index]
				# check if list
				if type(n[index]) == list:
					# go through list
					for listIndex in range(len(n[index])):
						self.result -= n[index][listIndex]
				# check if tuple
				if type(n[index]) == tuple:
					# go through tuple
					for tupleIndex in range(len(n[index])):
						self.result -= n[index][tupleIndex]

		# if restOfArg is provided
		if restOfArg is not None:
			# run through the restOfArg tuple values
			for index in range(len(restOfArg)):

				# check if list
				if type(restOfArg[index]) == list:
					# run through the list
					for listIndex in range(len(restOfArg[index])):
						# if int
						if type(restOfArg[index][listIndex]) == int:
							self.result -= restOfArg[index][listIndex]
						# if list
						if type(restOfArg[index][listIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][listIndex])):
								self.result -= restOfArg[index][listIndex][nestedListIndex]
						# if tuple
						if type(restOfArg[index][listIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][listIndex])):
								self.result -= restOfArg[index][listIndex][nestedTupleIndex]


				# check if integer
				if type(restOfArg[index]) == int:
					self.result -= restOfArg[index]

				# check if tuple
				if type(restOfArg[index]) == tuple:
					# run through the tuple
					for tupleIndex in range(len(restOfArg[index])):
						# if int
						if type(restOfArg[index][tupleIndex]) == int:
							self.result -= restOfArg[index][tupleIndex]
						# if list
						if type(restOfArg[index][tupleIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][tupleIndex])):
								self.result -= restOfArg[index][tupleIndex][nestedListIndex]
						# if tuple
						if type(restOfArg[index][tupleIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][tupleIndex])):
								self.result -= restOfArg[index][tupleIndex][nestedTupleIndex]
		# return
		return self

		def result(self):
			print self.result

md1 = MathDojo()
md1.add(2).add(2,5).subtract(3,2)
print 'Your result: {}'.format(md1.result)


md2 = MathDojo()
md2.add(([(2,2),2]),(2,2,2),2,([2,2])).subtract((1,1),[1,(1,1)])
print 'Your result: {}'.format(md2.result)


'''
BONUS FEATURES:
(1) [DONE] setup add() method so a lists can contain tuples or lists, and tuples can contain tuples or lists
(2) [DONE] setup subtract() method so lists/tuples can contain other lists or tuples (or integers)
'''