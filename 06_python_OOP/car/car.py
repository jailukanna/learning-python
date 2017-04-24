# Car Python OOP - Tim Knab

class Car(object):
	def __init__(self, price, speed, fuel, mileage, tax=None):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15 * 100
		else:
			self.tax = 0.12 * 100
		print 'New car created!'
		self.display_all()

	def display_all(self):
		print 'Price: ${} \nSpeed: {}mph \nFuel: {} \nMileage: {}mpg \nTax: {}%\n'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)