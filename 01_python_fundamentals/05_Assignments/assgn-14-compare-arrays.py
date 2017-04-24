'''
Write a program that compares two lists and prints a message depending on if
the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and
list_two. If both lists are identical print "The lists are the same". If they
are not identical print "The lists are not the same." Try the following test
cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
'''

def compare_arrays(list1, list2):
    if ((type(list1) is list) and (type(list2) is list)):
        if (list1 == list2):
            print 'The lists are the same.'
            return 'The lists are the same.'
        else:
            print 'The lists are not the same.'
            return 'The lists are not the same.'
    else:
        print 'These are not lists.'
        return 'Error: These are not lists.'

compare_arrays([1,2,5,6,2],[1,2,5,6,2])
compare_arrays([1,2,5,6,5],[1,2,5,6,5,3])
compare_arrays([1,2,5,6,5,16],[1,2,5,6,5])
compare_arrays(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])
compare_arrays(['celery','carrots','bread','milk'],['celery','carrots','bread','milk'])
