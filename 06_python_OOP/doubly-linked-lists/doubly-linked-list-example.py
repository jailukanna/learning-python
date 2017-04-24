'''A completely naive implementation of doubly linked lists.
Yeah, it sucks.
I'll make an __iter__() and next() [__next__() in 3.x] method later.
'''
class Node:
	def __init__(self, data, prior, next): #prior = prev <- For those familiar with doubley LL's.
		#Normally these are pointers, feelsbadman.
		self.data = data
		self.prior = prior
		self.next = next
	 
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_val, traceback):
		#lol, I just need this so the context manager (with) can be used.
		return None
		
	def __str__(self):
		return str(self.data)
		
class DoubleyList: #I don't really know what to name this.
		
	def __init__(self):
		#Still feelsbadman.  just for reference, the head is someList[0].
		self.head = None
		self.tail = None
		self.length = 0
	
	
	def __Append(self, data): #Append!
		
		nodeToAdd = Node(data, None, None)
		if (self.head == None):
			self.head = nodeToAdd
			self.tail = nodeToAdd
		else:
			#Sets up our node pointing at the one before it and None for the one ahead (default value of class definition).
			nodeToAdd.prior = self.tail
			#Points the current tail's next to the new node we just made.
			self.tail.next = nodeToAdd
			#Makes the new node we just made the tail.
			self.tail = nodeToAdd
		
		self.length += 1
		
	def Append(self, data):
		if ( (data) or (data is False) or (type(data) == str) or (data == 0) ):
			self.__Append(data)
		else:
			raise TypeError("I don't want you to be able to Append(NoneType).  No.")
	
	
	def __PopIndex(self, indTarg ): #Dumb version, crawls from head only.
		#Crawl to index we want to pop.
		target = self.head
		for i in xrange(indTarg):
			target = target.next
			
		#Set priorNode and nextNode for .prior/.next manipulation.
		priorNode = target.prior
		nextNode = target.next
		
		#If there are no more nodes in the list...
		if ( (priorNode == None) and (nextNode == None) ):
			#Update tail/head AND length and return.
			self.head = None
			self.tail = None
			self.length -= 1
			
			return target.data
		
		#See __PopLast/__PopFirst
		with target as toBePopped:
			#Try to cut out the toBePopped node.  Note: Will throw errors if nextNode/priorNode are NoneTypes, so we use a try/except statement.
			try:
				priorNode.next = nextNode
			except:
				#Okay, this is abit tricky.  If there is no priorNode, then that means we just popped the first element.  This means that the next element after the one we're popping becomes the new head.
				self.head = nextNode
			try:
				nextNode.prior = priorNode
			except:
				self.tail = priorNode #Definitely tricky.  If there is no nextNode (throws NoneType error), that means that we're popping the end of the list.  If we pop the end of the list, then we also need to update the tail.
			
			self.length -= 1
			return toBePopped.data
				
	def __PopLast(self): #Faster than crawling through the list.
		#Context-manager to make sure that the node we're removing is deleted by the garbage collector.
		with self.tail as toBePopped:
			#Set the tail as the prior node.
			self.tail = toBePopped.prior
			#Check if there's anything actually left in the list.
			if ( self.tail == None ):
				#If there's nothing in the list left, update the head AND length and return the popped data.
				self.head = None
				self.length -= 1
				return toBePopped.data
			#Set the pointer of the tail to none (since we're going to delete what it once pointed at).
			self.tail.next = None
			#Update the length.
			self.length -= 1
			
			#Return the popped item.
			return toBePopped.data
	
	def __PopFirst(self): #Unused function, just to show how it'd be done.
		#Context-manager to make sure that the node we're removing is deleted by the garbage collector.
		with self.head as toBePopped:
			#Set the head to the one the current head is pointing at.
			self.head = toBePopped.next
			
			#Check if there's anything actually left in the list.
			if ( self.head == None ):
				#If there's nothing in the list left, update the tail AND length and return the popped data.
				self.tail = None
				self.length -= 1
				return toBePopped.data
				
			#Set the new head's prior pointer to None (because we're deleting what it was pointing at).
			self.head.prior = None
			#Update length.
			self.length -= 1
			
			#Return popped item.
			return toBePopped.data
		
	def Pop(self, indexer = -1): #Forcefully setting a default value.  Remember, this takes an INDEX, not an element number.  Defaults to popping last element.  Default: __PopLast()

		#Catcher for default behavior.
		if ( (indexer == -1) or (indexer == (self.length - 1)) ):
			return self.__PopLast()
		elif ( indexer in xrange(self.length) ):
			return self.__PopIndex(indexer)
		else:
			raise IndexError("Yo, can't pop out of the list's range man.  List has: %d elements." % self.length)
	
	
	def __InsertAt(self, data, indTarg):  #Another dumb version, crawls from head only.   Adds AFTER index given.  This only triggers if you're not adding at the end or if the list is NOT empty or if the list does NOT contain only 1 node (see: InsertAt()).
		target = self.head
		for i in xrange(indTarg):
			target = target.next
			
		nextNode = target.next
		
		nodeToAdd = Node(data, None, None)
		
		#Insert the node and update length.
		target.next = nodeToAdd
		nodeToAdd.prior = target
		nodeToAdd.next = nextNode
		nextNode.prior = nodeToAdd
		self.length += 1
		
	def InsertAt(self, data, indexer = -1): #Default behavior (data, but no index specified): __Push()
	
		#Default behavior handler.  I didn't want to fill if you insert out of range.
		if ( (indexer == (self.length - 1)) or (self.length == 0) ):
			self.__Append(data)
		elif (indexer == -1):
			self.Push(data)
			'''
		elif( indexer == 0 ): #This is wrong.
			self.__Push(data)
			'''
		elif ( (indexer in xrange(self.length)) ):
			self.__InsertAt(data, indexer)
		else:
			raise IndexError('No, you cannot insert things that are outside of the current range.  Use Append()/Push() first to expand the size.')
	

	def __Push(self, data): #Pushes an element at the front only.
	
		nodeToAdd = Node(data, None, None)
		
		nodeToAdd.next = self.head 
		self.head.prior = nodeToAdd
		self.head = nodeToAdd
		
		self.length += 1
	
	def Push(self, data):
		
		#This is cheeeeeeese.
		if ( (data) or (data is False) or (type(data) == str) or (data == 0) ):
			if ( self.length == 0 ):
				self.__Append(data)
			else:
				self.__Push(data)
		else:
			raise TypeError("I don't want you to be able to Push(NoneType).  No.")
	
	
	def __InList(self, searchArg): #Another dumb version, crawls from head only. :C
		temp = self.head
		
		for i in xrange(self.length):
			if (temp.data is searchArg):
				return True
			
			temp = temp.next
		
		return False
		
	def InList(self, searchArg):
		if ( type(searchArg) == list ):
			raise TypeError("This function isn't built to handle lists yet.")
		else:
			return self.__InList(searchArg)
	
	def Empty(self): #Empties the list.
		for i in xrange(self.length):
			self.Pop()

	def Copy(self): #Makes a "deep" copy of the list.  Both for internal and external use.
		copiedList = DoubleyList()
		
		for i in xrange(self.length):
			copiedList.Append( self.GetByIdx(i) )
			
		return copiedList	
		
	def Min(self): #Slow O(N) search for min.
		min = self.head.data
		selector = self.head
		for i in xrange(self.length):
			if (selector.data < min):
				min = selector.data
			
			selector = selector.next
		
		return min
	
	def Max(self): #Slow O(N) search for max.
		max = self.head.data
		selector = self.head
		
		for i in xrange(self.length):
			if (selector.data > max):
				max = selector.data
				
			selector = selector.next
		
		return max
	
	def __Combine(self, setB): #Combines any two DoubleyList sets together.  Set(A) + Set(B) = Combine(A, B)   where setA is the self of this method.  Typically, we'de operator overload the +/- signs to handle set operations...But I'm waiting on an Answer from Martin regarding which approach is better.  For now, I'll just make this Combine() function, and I'll expand it into operator overloading later (It's honestly the exact same thing anyway).  The only reason this isn't a class method is because I ended up overloading the + operator.
	
		#Meld the head of setB and the tail of setA.
		self.tail.next = setB.head
		setB.head.prior = self.tail
		
		#Set the tail of setA to the tail of setB once they've been attached.  Don't forget to update length.
		self.tail = setB.tail
		self.length += setB.length 	
		
		return self
	
	
	def __GetByIdx(self, indexer): #RETURNS THE NODE!!!!!!!!!!!!!!
		targNode = self.head
		
		for i in xrange(indexer):
			targNode = targNode.next
			
		return targNode
	
	def GetByIdx(self, indexer): #RETURNS THE DATA AT INDEXER.
		
		if (type(indexer) != int):
			raise TypeError('Error, index supplied to get request was not a valid integer.')
			
		if (indexer < 0):
			indexer = self.length + indexer
			
		if ( indexer in xrange(self.length) ):
			return self.__GetByIdx(indexer).data
		else:
			raise IndexError("No, you cannot retrieve something that's outside the list's range.")
			
	
	def __BubbleSort(self): #Slow AF, this is an in-place sort and honestly should almost never be used, see: Qsort().
		
		sorted = False
		
		while (not sorted):
			sorted = True
			targNode = self.head
			
			for i in range(self.length - 1):
				nextNode = targNode.next
				
				if (nextNode.data < targNode.data):
					self.InsertAt( self.GetByIdx(i), (i+1) )
					self.Pop(i)
					sorted = False
				

				targNode = nextNode
	
	def __Qsort(self):  #Yo, this dumps the current list to sort.  Going to wrap this function in a copy function in order to not alter the list.
		less = DoubleyList()
		equiv = DoubleyList()
		greater = DoubleyList()
		#print 'QSORT CALLED'
		if (self.length > 1):
			pivot = self.head.data
			#print 'PIVOT: ' + str(pivot)
			for i in xrange(self.length):
				temp = self.Pop()
				
				#print 'Temp: ' + str(temp)
				
				if ( temp < pivot ):
					less.__Append(temp)
				elif ( temp == pivot ):
					equiv.__Append(temp)
				elif ( temp > pivot ):
					greater.__Append(temp)
			
			#print less
			#print equiv
			#print greater
			return less.__Qsort() + equiv + greater.__Qsort()
		else:
			return self
		
	def Sort(self, alterSelf = True): #Toggle to choose whether it just alters the list it's in or not.  Got it working.  Nasty though, clean it up.  I dont' know whether a copy is necessary.  Default behavior: Overwrite list.  Will always return the sorted list no matter what option is used. <- Nicer than Python built-in.  Inefficiently written, needs work.
		
		if ( type(alterSelf) != bool ):
			raise TypeError('Invalid input type for Sort(). Must be True/False value.')
		else:
			copiedList = self.Copy()
			copiedList = copiedList.__Qsort()
			
			if (alterSelf):
				#Copy the list to this self.
				self.head = copiedList.head
				self.tail = copiedList.tail
				return self
			else:
				return copiedList
	
	
	def __Reverse(self, alterSelf = True): #Oh, implement this type of strategy in Sort.
		copiedList = self.Copy()
		
		if (alterSelf):
			self.Empty()
			
			for i in xrange(copiedList.length):
				self.Append( copiedList.Pop() ) #Memory concern?
		
			return self
		else:
			returnCopy = copiedList.Copy()
			returnCopy.Empty()
			
			for i in xrange(copiedList.length):
				returnCopy.Append( copiedList.Pop() )
				
			return returnCopy
					
	def Reverse(self, alterSelf = True): #In-place reverse.  Default behavior: Overwrite list.
		if ( type(alterSelf) != bool):
			raise TypeError('Invalid input type to Reverse(), must be True/False value.')
		else:
			return self.__Reverse(alterSelf) 
	


		
	'''All override/overload handlers will go below here.'''
	
	def __len__(self): #len(obj) handler.
		return self.length
	
	def __add__(self, otherList=None): # + Operator overload.
	
		if (otherList.head == None):
			return self
		elif (self.head == None):
			return otherList
		else:
			return self.__Combine(otherList)
		
	def __str__(self): #Print handler.
		if ( self.length == 0 ):
			return '[]'
			
		rString = "["
		temp = self.head
		for i in range(self.length - 1):
			rString += str(temp.data) + ", " 
			
			temp = temp.next
		
		rString += str(temp.data) + "]"
		return rString
	

def tester():
	import random

	lister = DoubleyList()
	testList = []
	for i in range(1000):
		temp = random.randint(0, 100)
		lister.Append(temp)
		testList.append(temp)
		
	return lister, testList


if __name__ == "__main__":
	import time
	
	
	lister, testList = tester()
	lister2 = DoubleyList()
	
	print lister
	print '-------------------'
	testList.sort()
	start = time.time()
	lister.Sort()
	end = time.time()
	print lister
	print testList
	print 'Time elapsed for sorting: ' + str(end - start) + ' seconds.'


	


	







