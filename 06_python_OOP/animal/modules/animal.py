class Animal(object):
  def __init__(self, name=None):
    self.health = 100
    self.name = name

  def walk(self):
    self.health -= 1
    return self

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

