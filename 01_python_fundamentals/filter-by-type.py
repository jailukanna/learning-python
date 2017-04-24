'''
Write a program that, given some value, tests that value for its type. Here's
what you should do for each type:

#Integer
If the integer is greater than or equal to 100 print "That's a big number!" If
the integer is less than 100 print "That's a small number"

#String
If the string is greater than or equal to 50 characters print "Long sentence."
If the string is shorter than 50 characters print "Short sentence."

#List
If the length of the list is greater than or equal to 10 print "Big list!" If
the list has fewer than 10 values print "Short list."
'''

def filter_type(value):
    # if integer:
    if (type(value) is int):
        if (value >= 100):
            print "That's a big number!"
        else:
            print "That's a small number."
    # if string:
    if (type(value) is str):
        if (len(value) >= 50):
            print "Long Sentence."
        else:
            print "Short Sentence."
    # if list:
    if (type(value) is list):
        if (len(value) >= 10):
            print "Big List!"
        else:
            print "Short List!"

filter_type([1,2,3,4,5,6,7,8,9])
