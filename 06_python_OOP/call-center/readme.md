# Call Center
You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

You will create two classes. One class should be Call, the other CallCenter.

Call():
Create your call class with an init method. Each instance of Call() should have a few attributes:

- unique id

- caller name

- caller phone number

- time of call

- reason for call

The call class should have a display method that prints all call attributes.

CallCenter():
Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:

- calls: should be a list of call objects

- queue size: should be the length of the call list

The call center class should have an add method that adds a new call to the end of the call list

The call center class should have a remove method that removes the call from the beginning of the list (index 0).

The call center class should have a method called info that shows the name and phone number for each call in the queue as well as the length of the queue.

You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!

Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.

Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
