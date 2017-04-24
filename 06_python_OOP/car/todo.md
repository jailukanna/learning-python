Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

A sample output would be like this:

	Price: 2000
	Speed: 35mph
	Fuel: Full
	Mileage: 15mpg
	Tax: 0.12


	Price: 2000
	Speed: 5mph
	Fuel: Not Full
	Mileage: 105mpg
	Tax: 0.12


	Price: 2000
	Speed: 15mph
	Fuel: Kind of Full
	Mileage: 95mpg
	Tax: 0.12


	Price: 2000
	Speed: 25mph
	Fuel: Full
	Mileage: 25mpg
	Tax: 0.12


	Price: 2000
	Speed: 45mph
	Fuel: Empty
	Mileage: 25mpg
	Tax: 0.12


	Price: 20000000
	Speed: 35mph
	Fuel: Empty
	Mileage: 15mpg
	Tax: 0.15