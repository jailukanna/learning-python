#########
#
# 	BIKE
#
#########

	+ [DONE] Create a new class called Bike with the following properties/attributes:
		+ [DONE] price
		+ [DONE] max_speed
		+ [DONE] miles

	+ [DONE] Create 3 instances of the Bike class.

		+ Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); 

		+ [DONE] In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

	+ [DONE] Add the following functions to this class:

		+ [DONE] displayInfo() - have this method display the bike's price, maximum speed, and the total miles.

		+ [DONE] ride() - have it display "Riding" on the screen and increase the total miles ridden by 10

		+ [DONE] reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...

	+ [DONE] Have the first instance ride three times, reverse once and have it displayInfo(). 

	+ [DONE] Have the second instance ride twice, reverse twice and have it displayInfo(). 

	+ [DONE] Have the third instance reverse three times and displayInfo().

	+ [DONE] What would you do to prevent the instance from having negative miles?

		+ Solution: Add the following code into the reverse() method:

				if self.miles < 0:
				self.miles = 0
			print 'Total miles traveled: {}.mi.'.format(self.miles)
