class MathDojo(object):
	def __init__(self, result=0):
		self.result = 0

	def add(self, n, *restOfArg):
		if type(n) == list:
			for index in range(len(n)):
				if type(n[index]) == int:
					self.result += n[index]
				if type(n[index]) == list:
					for listIndex in range(len(n[index])):
						self.result += n[index][listIndex]
				if type(n[index]) == tuple:
					for tupleIndex in range(len(n[index])):
						self.result += n[index][tupleIndex]
		if type(n) == int:
			self.result += n
		if type(n) == tuple:
			for index in range(len(n)):
				if type(n[index]) == int:
					self.result += n[index]
				if type(n[index]) == list:
					for listIndex in range(len(n[index])):
						self.result += n[index][listIndex]
				if type(n[index]) == tuple:
					for tupleIndex in range(len(n[index])):
						self.result += n[index][tupleIndex]
		if restOfArg is not None:
			for index in range(len(restOfArg)):
				if type(restOfArg[index]) == list:
					for listIndex in range(len(restOfArg[index])):
						if type(restOfArg[index][listIndex]) == int:
							self.result += restOfArg[index][listIndex]
						if type(restOfArg[index][listIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][listIndex])):
								self.result += restOfArg[index][listIndex][nestedListIndex]
						if type(restOfArg[index][listIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][listIndex])):
								self.result += restOfArg[index][listIndex][nestedTupleIndex]
				if type(restOfArg[index]) == int:
					self.result += restOfArg[index]
				if type(restOfArg[index]) == tuple:
					for tupleIndex in range(len(restOfArg[index])):
						if type(restOfArg[index][tupleIndex]) == int:
							self.result += restOfArg[index][tupleIndex]
						if type(restOfArg[index][tupleIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][tupleIndex])):
								self.result += restOfArg[index][tupleIndex][nestedListIndex]
						if type(restOfArg[index][tupleIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][tupleIndex])):
								self.result += restOfArg[index][tupleIndex][nestedTupleIndex]
		return self

	def subtract(self, n, *restOfArg):
		if type(n) == list:
			for index in range(len(n)):
				if type(n[index]) == int:
					self.result -= n[index]
				if type(n[index]) == list:
					for listIndex in range(len(n[index])):
						self.result -= n[index][listIndex]
				if type(n[index]) == tuple:
					for tupleIndex in range(len(n[index])):
						self.result -= n[index][tupleIndex]
		if type(n) == int:
			self.result -= n
		if type(n) == tuple:
			for index in range(len(n)):
				if type(n[index]) == int:
					self.result -= n[index]
				if type(n[index]) == list:
					for listIndex in range(len(n[index])):
						self.result -= n[index][listIndex]
				if type(n[index]) == tuple:
					for tupleIndex in range(len(n[index])):
						self.result -= n[index][tupleIndex]
		if restOfArg is not None:
			for index in range(len(restOfArg)):
				if type(restOfArg[index]) == list:
					for listIndex in range(len(restOfArg[index])):
						if type(restOfArg[index][listIndex]) == int:
							self.result -= restOfArg[index][listIndex]
						if type(restOfArg[index][listIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][listIndex])):
								self.result -= restOfArg[index][listIndex][nestedListIndex]
						if type(restOfArg[index][listIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][listIndex])):
								self.result -= restOfArg[index][listIndex][nestedTupleIndex]
				if type(restOfArg[index]) == int:
					self.result -= restOfArg[index]
				if type(restOfArg[index]) == tuple:
					for tupleIndex in range(len(restOfArg[index])):
						if type(restOfArg[index][tupleIndex]) == int:
							self.result -= restOfArg[index][tupleIndex]
						if type(restOfArg[index][tupleIndex]) == list:
							for nestedListIndex in range(len(restOfArg[index][tupleIndex])):
								self.result -= restOfArg[index][tupleIndex][nestedListIndex]
						if type(restOfArg[index][tupleIndex]) == tuple:
							for nestedTupleIndex in range(len(restOfArg[index][tupleIndex])):
								self.result -= restOfArg[index][tupleIndex][nestedTupleIndex]
		return self

		def result(self):
			print self.result

md1 = MathDojo()
md1.add(2).add(2,5).subtract(3,2)
print 'Your result: {}'.format(md1.result)

md2 = MathDojo()
md2.add(([(2,2),2]),(2,2,2),2,([2,2])).subtract((1,1),[1,(1,1)])
print 'Your result: {}'.format(md2.result)
# i said no comments, but just kidding 'cuz here's a few:
# note that nested tuples or lists work in the add() and subtract() methods
# but holy cow the code is lengthy -- how can this be refactored?