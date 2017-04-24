##########
#
#	Animal Project - Python OOP Inheritance Project
#
##########

	+ [DONE] Create a class called Animal with the following attributes: 
		+ [DONE] name
		+ [DONE] health 

	+ [DONE] Give the animal following three methods: 
		+ [DONE] walk
		+ [DONE] run
		+ [DONE] displayHealth

	+ [DONE] Give a new animal a health of 100 when it gets created. 

	+ [DONE] When a walk() method is invoked, have the health decrease by 1. 

	+ [DONE] When a run() method is involved, have the health decrease by 5. 

	+ [DONE] When a displayHealth() method is invoked, display on screen the name of the Animal and the health.

	+ [DONE] Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.

// this is where you're going to create a child class

	+ [DONE] Now, create another class called Dog that inherits everything that the Animal does and has, but 

		+ [DONE] 1) have the default health be 150 and (*NOTES* Used SUPER init)
		+ [DONE] 2) add a new method called pet, which when invoked, increases the health by 5. 

	+ [DONE] Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

// another child class

	+ Now, create another class called Dragon that also inherits everything from Animal, but 
		+ 1) have the default health be 170 and 
		+ 2) add a new method called fly, which when invoked, decreased the health by 10. 

	+ Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).

Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-: