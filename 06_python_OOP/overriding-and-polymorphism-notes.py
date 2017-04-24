#######
#
#	OVERRIDING
#
######


# if you have an instance where you want a child object to overwrite a parent class,
# you can do so by overriding it via writing the same class name and defining it --
# the new class name will override the parent.

# Here's an example:

class Parent(object):
	def method_a(self):
		print "invoking PARENT method_a!"

# this class Child, because we've passed the parameter 'Parent' inherits Parent's properties
# however we will define the same class--thus Child's version will override the properties 
# of the Parent's method_a
class Child(Parent):
	def method_a(self):
		print 'invoking CHILD method_a!'

dad = Parent()
son = Child()
dad.method_a()
son.method_a() # this will override the parent

# the printout will be:
# 'invoking PARENT method_a!'
# 'invoking CHILD method_a!'

#######
#
#	POLYMORPHISM
#
######

# sometimes you might want to create some child instances which overriding classes, but you don't
# really want the parent to have any initial value
# to do this, when you create your parent class, you can call a `raise NotImplementedError` statement (i think this is a statement)

class Person(object):
	def pay_bill(self):
		raise NotImplementedError
		# basically, pay_bill does nothing for Person(), but..

# this child class does however
class Millionaire(Person):
	def pay_bill(self): # same class being overriden
		print 'Here you go! Keep the change!'

class GradStudent(Person):
	def pay_bill(self):
		print 'Can you loan me some money?'

# even though pay_bill is defined in the parent function, the `raise NotImplementedError` causes nothing to happen.
# however, with Millionare.pay_bill() or GradStudent.pay_bill(), unique print statements are rendered.
# this allows us to create a class in our parent function that we don't want the parent object to necessarily do anything


