# Bike Python OOP - Tim Knab

class Bike(object):
	def __init__(self, price=None, max_speed=None, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
		print 'New bike created!'

	def displayInfo(self):
		print 'Your Summary for: Price: ${}, Max Speed: {}mph, Total Miles: {}mi'.format(self.price, self.max_speed, self.miles)

	def ride(self):
		print 'Riding...'
		self.miles += 10
		print 'Total miles traveled: {}mi.'.format(self.miles)

	def reverse(self):
		print 'Reversing...'
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		print 'Total miles traveled: {}.mi.'.format(self.miles)

bike_one = Bike(100, 25)
for count in range(3):
	bike_one.ride()
bike_one.reverse()
bike_one.displayInfo()

bike_two = Bike(150, 30)
for count in range(2):
	bike_two.ride()
for count in range(2):
	bike_two.reverse()
bike_two.displayInfo()

bike_three = Bike(200, 40)
for count in range(3):
	bike_three.reverse()
bike_three.displayInfo()