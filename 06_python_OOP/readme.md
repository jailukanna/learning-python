# Python Object Oriented Programming:
See the `/animal` assignment for detailed notes on how to create Classes, as well
as Parent and Child classes (with unique properties). It can seem daunting at first,
but if you read the notes and study the examples, you'll see that the structure
is actually pretty self forward. The takeways are to:

1. Be sure to create an __init__ method (this is your constructor).
2. Make sure you define any instantiated values as parameters in your __init__ method.
3. Be sure to `return self` in any instance methods, else you won't be able to Chain,
   nor will your modified property values be saved otherwise.
4. Follow the examples for the specific syntax when using `super()` to create
   Child classes.

*Notes*: It seems confusing as well, but read the notes and it will
make more sense. Essentially, `super(<child_class>, <self>)` takes two parameters.
The first being the name of the Child class and the second is itself. Also,
when you define your Child classes, be sure to use the name of the Parent as
its property. ie, `class Dog(Animal)`, `Dog` is the name of the Child class,
while `Animal` is the argument given which is the name of the Parent class.
This allows the new class access to all of the Parent attributes.

*Further Notes*: The `/animal` assignment is also a good project to examine the
syntax for importing modules.
