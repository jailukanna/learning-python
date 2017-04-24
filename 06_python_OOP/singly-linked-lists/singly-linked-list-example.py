# this is our node object
class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# this is our singly linked list object
class SinglyLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def addBack(self, value):
		# create a new node with the value
		newNode = Node(value)
		# if list is empty
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			# point tail to new node
			self.tail.next = newNode
			# set tail to new node
			self.tail = newNode

	def addFront(self, value):
		# create new node
		newNode = Node(value)
		# set old head to point to new node
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			# store old head
			last_head = self.head
			# set head to new node
			self.head = newNode
			# point head to old head
			self.head.next = last_head

	def insertAfter(self, targetNode, value):
		# create new node
		newNode = Node(value)
		# find target node to insert
		node = self.head
		if node == None:
			print 'There aren\'t any nodes to insert before!'
		else:
			found = None
			# search nodes
			while node.next:
				if node.value == targetNode:
					found = True
					afterInsert = node.next # we will connect our new node to this
					node.next = newNode # sets our current node's next to our new node
					newNode.next = afterInsert # sets our new node's next to what was previously in its position
					node = node.next # continues through while loop
				else:
					node = node.next
			if found != True:
				print 'Your target node of {} was not found in the list!'.format(targetNode)

	def insertBefore(self, targetNode, value):
		# create new node
		newNode = Node(value)
		# find target node to insert
		node = self.head
		if node == None:
			print 'There aren\'t any nodes to insert before!'
		else:
			found = False
			# search nodes
			while node:
				if node.next == None:
					break
				if node.next.value == targetNode:
					found = True
					newNode.next = node.next
					node.next = newNode
					break
				else:
					node = node.next
			if found != True:
				print 'Your target node of {} was not found in the list!'.format(targetNode)

	def removeNode(self, destroyNode):
		# find the node
		node = self.head
		while node:
			if node.next == None:
				break
			else:
				found = False
				if node.next.value == destroyNode:
					found = True
					beforeDestroy = node
					afterDestroy = node.next.next
					beforeDestroy.next = afterDestroy
					del self
				node = node.next

		if found != True:
			print 'Node to delete was not found.'

	def reverseList(self):
		prev = self.head
		next = self.head.next
		prev.next = None

		while next:
			temp = next.next
			next.next = prev
			prev = next
			next = temp

		self.head, self.tail = self.tail, self.head


	def printAll(self):
		# setting our variable below allows us to access properties of head
		node = self.head
		if node == None:
			print 'Nothing in the list!'
		else:
			while node:
				print 'Your node value is: {}.'.format(node.value)
				node = node.next

# create node instances
names = SinglyLinkedList()

# invoke new methods
names.addBack('Julianna')
names.addBack('Roger')
names.addBack('Bill')
names.addFront('Tim')
names.addFront('Mary')
names.addFront('William')
names.insertAfter('Tim','Chris')
names.insertAfter('Chris', 'Vida')
names.insertBefore('Tim','John')
names.insertBefore('John', 'Greg')
names.removeNode('Roger')
names.reverseList()

# invoke new methods
names.printAll()


'''
[DONE]PrintAllVals
[DONE]AddBack(val)
[DONE]AddFront(val)
[DONE]InsertBefore(nextVal, val)
[DONE]InsertAfter(preval, val)
[DONE] RemoveNode(val)
ReverseList()
'''

