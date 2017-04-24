# since we created bulb_classes.py, let's go ahead and run some tests:

import unittest
from bulb_classes import LightBulb, LightBulbFactory

class LightBulbTest(unittest.TestCase):
	# we're going to use the method called setUp() [built into unittest] to create an intial instance of bulb_factory
	# and a new light bulb

	# so we don't have to type the same things over and over
	# we can stash things we'll want for every test into setUp() method
	# note that this method below, setUp() will run after every test
	def setUp(self):
		self.bulb_factory = LightBulbFactory()
		self.bulb = self.bulb_factory.create_bulb("GE")

	# let's test if the created bulb is indeed an instance of LightBulb
	def testNewBulbIsLightBulb(self):
		return self.assertIsInstance(self.bulb, LightBulb)

	# test the created bulb to make sure it has a brand
	def testBulbHasBrand(self):
		return self.assertEqual("GE", self.bulb.brand)

	# test the created bulb to make sure its off by default
	def testBulbDefaultOff(self):
		return self.assertEqual(False, self.bulb.on_or_off())

	# test to see if we can switch the bulb on from the off status
	def testTurnOnBulb(self):
		self.bulb.switch_on()
		return self.assertEqual(True, self.bulb.on_or_off())

# run the tests
if __name__ == "__main__":
	unittest.main()

# similar to setUp(), we can use tearDown(), a method that can run after every test that will clean things up
# google around for an xample of when to use tearDown() [perhaps if you want to remove something after a test runs]

'''

######
#
#	More notes about TDD process:
#
######

	+ This is really hard to do during our Bootcamp process
	+ However, this is something that you can utilize if you are developing more slowly to make sure everything is as Bug Free as possible
	+ This might be an important process if working to create features for a big project, like Amazon, that has huge implications if errors
	+ Or if you're building features that will be used for a LONG time and MUST be bug-free
	+ Maybe this is important when building a public facing API

'''

