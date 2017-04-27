'''
Create an Animal class and give it the below attributes and methods. Extend the
Animal class to two child classes, Dog and Dragon.

# Objective
The objective of this assignment is to help you understand inheritance. Remember
that a class is more than just a collection of properties and methods. If you want
to create a new class with attributes and methods that are already defined in another
class, you can have this new class inherit from that other class (called the parent)
instead of copying and pasting code from the original class. Child classes can access
all the attributes and methods of a parent class AND have new attributes and methods
of its own, for child instances to call. As we see with Wizard / Ninja / Samurai
(that are each descended from Human), we can have numerous unique child classes
that inherit from the same parent class.

# Animal Class
Create a class called Animal with the following attributes: name, and health.
Give the Animal the following three methods: walk, run, and displayHealth. Give
a new Animal 100 health when it gets created. When the walk() method is invoked,
have the health decrease by 1. When the run() method is invoked, have the health
decrease by 5. When the displayHealth() method is invoked, display on screen the
name of the Animal and the health.

Create an instance of the Animal, have it walk() three times, run() twice, and
finally displayHealth() to confirm that the health attribute has changed.

# Dog Class
Create a class called Dog that inherits everything that the Animal does, except
the Dog class should have a default health of 150 and a new method called pet(),
which increases the health by 5. Have the Dog walk() three times, run() twice,
pet() once, and have it displayHealth().

# Dragon Class
Finally, create a class called Dragon that also inherits everything from Animal.
The Dragon class should have the default health be 170 and a new method called
fly(), which decreased the health by 10. Have the Dragon walk() three times,
run() twice, fly() twice, and have it displayHealth(). When the Dragon's
displayHealth() function is called, it should say 'this is a dragon!' before it
displays the default information. You can achieve this by calling the parent's
displayHealth() function.

Now try creating a new Animal and confirm that it can not call the pet() and fly()
methods, and it's displayHealth() is not saying 'this is a dragon!'. Also confirm
that your Dog class can not fly().
'''

# Import our Parent Class as a module:
from modules.animal import Animal

# Define our Child Class, using the Parent Class as a parameter (this will make
# `Dog` below inherit the properties of `Animal`):
class Dog(Animal):
	# note that the two lines below contain the word, `name`
	# this was put in here because when we are creating our Dog, we still want to
	# give it a `name` attribute value, so that the parent function is satisfied.
	# this dog will now take on the name 'Winston' because:
	# (1) we added `name` after our super reference, ie, `super(Dog, self).__init__(name)`
	# (2) we added `name` into our `def __init__(self, name)` statement
	def __init__(self, name):
		# `super` is Python's way of inheriting Parent classes.
		# For the parameters, you must provide the name of the Child class (in
		# this case `Dog`), along with `self` (required). You must also pass
		# any parameters in the Parent into the super's __init__ method. In the
		# example below, we pass `name`, so that our Child classes can pass along
		# the `name` to our Parent (which has `name=None` by default, unless one
		# is provided).
		super(Dog, self).__init__(name)
		# Once we've hooked into our Parent class using `super`, we can modify
		# or add properties to build off our Parent class. In our Parent, `health`
		# by default is `100`. However, in our Child Class of `Dog`, we're going
		# to change that to `150`.
		self.health = 150
	# Create another instance method of the Child Class `Dog` called `pet`. Note
	# that `pet()` is only accessible to the Child class `Dog`, and not the parent.
	def pet(self):
		# Add 5 to our `health` when the `Dog` is `Pet()`
		self.health += 5
		# Always be sure to return `self` if properties have been modified,
		# otherwise they won't save, nor will you be able to Chain methods.
		return self

# This instantiates our Child class `Dog` with the parameter (name) of `Winston`
dog1 = Dog('Winston')
# We can chain the methods to invoke one after another. Because our Child instance
# has been invoked with `Animal` as a Parent, we can also access Parent instance
# method functions as well.
dog1.walk().walk().walk().run().run().pet().displayHealth()

# Let's define another Child class, this time called `Dragon`, with some unique
# properties to both the parent and the previous Child class we created above:
class Dragon(Animal): # Be sure to pass `Animal` (the Parent class) to make a Child.
	# __init__ again which matches `__init__` parameters of Parent.
	def __init__(self, name): # must pass `self` as well as parent parameters.
		# invoke Super to tap into Parent, passing proper parameters:
		super(Dragon, self).__init__(name)
		# For our dragon, the instantiated `health` will have a value of 170.
		self.health = 170
	# Create an instance method for the Child class `Dragon`:
	def fly(self): # must pass `self`
		self.health -= 10
		return self # return `self` after a property has been modified.

# As we did previously, we can instantiate our Child class like this:
dragon1 = Dragon('Scarlett')
# And we can take that instance now and access parent methods, while also
# accessing our Child instance methods -- all of which can be chained together.
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
