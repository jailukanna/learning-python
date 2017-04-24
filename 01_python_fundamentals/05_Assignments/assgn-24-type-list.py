'''
Write a program that takes a list and prints a message for each element in the
list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its
data type. If the item is a string, concatenate it onto a new string. If it is
a number, add it to a running sum. At the end of your program print the string,
the number and an analysis of what the array contains. If it contains only one
type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of
unexpected input could you get?

#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The array you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# input
l = [2,3,1,7,4,12]
#output
"The array you entered is of integer type"
"Sum: 29"

# input
l = ['magical','unicorns']
#output
"The array you entered is of string type"
"String: magical unicorns"
'''

def type_list(custom_list):
    if (type(custom_list) is list):
        sum = 0
        string = ''
        int_status = False
        str_status = False
        for value in custom_list:
            # if int, add sum and set int status true:
            if (type(value) is int):
                sum += value
                int_status = True
            # if str, add to total string and set str status true:
            if (type(value) is str):
                string += value + " "
                str_status = True
        # Assess results above:
        # if mixed:
        if ((int_status == True) and (str_status == True)):
            print "The array you entered is mixed type."
            print "STRING: {}".format(string)
            print 'SUM: {}'.format(sum)
            return "The array you entered is mixed type.", string, sum
        # if string only:
        elif ((int_status == False) and (str_status == True)):
            print "The array you entered is of string type."
            print "STRING: {}".format(string)
            return "The array you entered is string type.", string
        # if integers only:
        elif ((int_status == True) and (str_status == False)):
            print "The array you entered is of integer type."
            print "SUM: {}".format(sum)
            return "The array you entered is integer type.", sum
    else:
        print "You must enter a list."
        return "You must enter a list."

type_list(['magical','unicorns'])
type_list([2,3,1,7,4,12])
type_list(['magical unicorns',19,'hello',98.98,'world'])
