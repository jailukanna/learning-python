# let's say we created the following file, and we'd like to run some tests
# go ahead and open /test_bulb.py after looking at this file

class LightBulb(object):
	def __init__(self, brand):
		self.is_on = False
		self.brand = brand

	def switch_on(self):
		self.is_on = True

	def switch_off(self):
		self.is_on = False

	def on_or_off(self):
		return self.is_on

class LightBulbFactory(object):
	def create_bulb(self, brand):
		new_bulb = LightBulb(brand)
		return new_bulb

