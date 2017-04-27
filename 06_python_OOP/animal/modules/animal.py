'''
When creating a class we want to make sure we pass `object` as a parameter. We also must
define a __init__ method which is utilized as the constructor function. The parameters
given to our __init__ function are utilized upon instance creation. In the event that
a parameter is optional, you may set it to `None` as seen in the __init__ method below.
In this scenario, if a name is not given, it will default to `None`, else, a name will be
assigned if the parameter is provided.
'''
class Animal(object):
  def __init__(self, name=None):
    self.health = 100
    self.name = name

  def walk(self):
    self.health -= 1
    return self # returning `self` saves the modified property and also allows us to Chain

  def run(self):
    self.health -= 5
    return self

  def displayHealth(self):
    if self.name is not None:
      print self.name + ' has {} health.'.format(self.health)
    else:
      print 'You didn\'t give a name!'
    return self

animal1 = Animal('animal')
animal1.walk().walk().walk().run().run().displayHealth()
