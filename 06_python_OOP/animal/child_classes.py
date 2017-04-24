from modules.animal import Animal

class Dog(Animal):
	# note that the two lines below contain the word, `name`
	# this was put in here because when we are creating our Dog, we still want to give it a `name` attribute value, so that the parent function is satisfied.
	# this dog will now take on the name 'Winston' because:
	# (1) we added `name` after our super reference, ie, `super(Dog, self).__init__(name)`
	# (2) we added `name` into our `def __init__(self, name)` statement
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	def pet(self):
		self.health += 5
		return self

dog1 = Dog('Winston')
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	def fly(self):
		self.health -= 10
		return self

dragon1 = Dragon('Scarlett')
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()

'''
// [DONE] another child class

	+ [DONE] Now, create another class called Dragon that also inherits everything from Animal, but 
		+ [DONE] 1) have the default health be 170 and 
		+ [DONE] 2) add a new method called fly, which when invoked, decreased the health by 10. 

	+ [DONE] Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).

Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:
'''