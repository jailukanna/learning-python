'''
Making Dictionaries
Create a function that takes in two lists and creates a single dictionary where
the first list contains keys and the second values. Assume the lists will be of
equal length.

Your first function will take in two lists containing some strings. Here are two
example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

Here's some help starting your function.

def make_dict(arr1, arr2):
  new_dict = {}
  # your code here
  return new_dict

Hacker Challenge:
If the lists are of unequal length, the longer list should be used for the keys,
the shorter for the values.
'''

def make_dictionaries_from_lists(list1, list2):
    output = {}
    print 'LIST 1: {}'.format(list1)
    print 'LIST 2: {}'.format(list2)
    counter = 0
    for value in list1:
        output[value] = list2[counter]
        counter += 1
    print 'OUTPUT: {}'.format(output)
    return output

print '\n'
print "~~~~~ TESTS ~~~~~~"
make_dictionaries_from_lists(["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"], ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"])
print '\n'
make_dictionaries_from_lists(["John", "James", "Judy", "Jacky", "Juniper", "JoJo", "Jose"], ["aluminum", "iron", "gypsum", "andesite", "gneiss", "granite", "cobalt"])

def unequal_dict_lists(list1, list2):
    output = {}
    counter = 0
    if len(list1) > len(list2):
        for value in list1:
            try:
                output[value] = list2[counter]
                counter += 1
            except IndexError:
                output[value] = "None"
                counter += 1
        print 'LIST 1 IS LONGEST:'
        print 'LIST 1: {}'.format(list1)
        print 'LIST 2: {}'.format(list2)
        print 'OUTPUT: {}'.format(output)
        return output
    if len(list2) > len(list1):
        for value in list2:
            try:
                output[value] = list1[counter]
                counter += 1
            except IndexError:
                output[value] = "None"
                counter += 1
        print 'LIST 2 IS LONGEST:'
        print 'LIST 2: {}'.format(list2)
        print 'LIST 1: {}'.format(list1)
        print 'OUTPUT: {}'.format(output)
        return output
    else:
        print "Lists cannot be compared."

print '\n'
print "~~~~~ HACKER CHALLENGE ~~~~~~"
unequal_dict_lists(["John", "James", "Judy", "Jacky", "Juniper", "JoJo", "Jose"], ["aluminum", "iron", "gypsum", "andesite", "gneiss", "granite"])
print '\n'
unequal_dict_lists(["John", "James", "Judy", "Jacky"], ["aluminum", "iron", "gypsum", "andesite", "gneiss", "granite"])
print '\n'
