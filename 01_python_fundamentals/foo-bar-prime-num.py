'''
Write a program that prints all the prime numbers and all the perfect squares
for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for whether it is prime
or a perfect square.

If it is a prime number print "Foo".
If it is a perfect square print "Bar".
If it is neither print "FooBar".

Do not use the python math library for this exercise. For example, if the number
you are evaluating is 25, you will have to figure out if it is a perfect square.
It is, so print "Bar".

What is a Prime Number?
A positive integer greater than 1 which has no other factors except 1 and the
number itself is called a prime number. 2, 3, 5, 7 etc. are prime numbers as
they do not have any other factors.

What is a Perfect Square?
An integer whom is a product of a some integer with itself. For example, 3x3 is
9, thefor 9 is a perfect square. 2x2 is 4, 4 is a perfect square. 7 is not a
perfect square.
'''

# Check if Perfect Square:
def is_square(positive_int):
    x = positive_int // 2
    seen = set([x])
    while x * x != positive_int:
        x = (x + (positive_int // x)) // 2
        if x in seen:
            return "{} is not a perfect square.".format(positive_int), False
        seen.add(x)
    return "{} is a perfect square.".format(positive_int), True


# Check if Prime Number:
def is_prime(positive_int):
    if positive_int > 1:
        # check if any factors:
        for x in range(2, positive_int):
            if (positive_int % x) == 0:
                return "{} is not a prime number.".format(positive_int), False
        else:
            return "{} is a prime number.".format(positive_int), True
    else:
        return "A prime number must be greater than 1.".format(positive_int), False

# Evaluate Number for Prime/Perfect for Foo Bar:
def foo_bar(positive_int):
    if is_prime(positive_int)[1] == True:
        return "Foo"
    if is_square(positive_int)[1] == True:
        return "Bar"
    if (is_prime(positive_int)[1] == False) and (is_square(positive_int)[1] == False):
        return "FooBar"

print "~~~~~ TESTS ~~~~~"
print "SQUARE:", is_square(101)
print "PRIME:", is_prime(101)
print "FOOBAR:", foo_bar(101)
print "~~~~~~~~~~~~~~~~~"

# # Run Tests for integers 100 - 100,000. Uncomment to enable!
# for i in range(100, 100000):
#     print "NUMBER: {} | FOOBAR: {}".format(i, foo_bar(i))
