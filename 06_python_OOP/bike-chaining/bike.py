# Bike Python OOP - Tim Knab

class Bike(object):
	def __init__(self, price=None, max_speed=None, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
		print 'New bike created!'

	def displayInfo(self):
		print 'Your Summary for: Price: ${}, Max Speed: {}mph, Total Miles: {}mi'.format(self.price, self.max_speed, self.miles)
		return self

	def ride(self):
		print 'Riding...'
		self.miles += 10
		# print 'Total miles traveled: {}mi.'.format(self.miles)
		return self

	def reverse(self):
		print 'Reversing...'
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		# print 'Total miles traveled: {}.mi.'.format(self.miles)
		return self

bike1 = Bike(100, 25)
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(150, 30)
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(200, 40)
bike3.reverse().reverse().reverse().displayInfo()
