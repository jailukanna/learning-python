'''
#Find and Replace
In this string: str = "It's thanksgiving day. It's my birthday,too!" print the
position of the first instance of the word "day". Then create a new string where
the word "day" is replaced with the word "month".
'''
print '### FIND & REPLACE ###'
str = "It's thanksgiving day. It's my birthday too!"
print '#STRING:', str
# Print idx of first instance of 'the'
print '#IDX:', str.index('day')

# Replace 'the' with 'month' using built in string method:
str = str.replace('day', 'month')
print '#REPLACE:', str


'''
#Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your
code should work for any list.
'''
print '### MIN & MAX ###'
def min_max(list):
    min, max = 0, 0
    print '#LIST:', list
    for x in list:
        if (x > max):
            max = x
        if (x < min):
            min = x
    print '#MIN: {}, MAX: {}'.format(min, max)
    return min, max

min_max([2,54,-2,7,12,98])
min_max([112,4,-32,72,13,8])

'''
#First and Last
Print the first and last values in a list like this one:
x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the
first and last values in the original list. Your code should work for any list.
'''
print '### FIRST & LAST ###'
def first_last(list):
    first = list[0]
    last = list[len(list)-1]
    print first, last
    print [first, last]
    return [first, last] # returns list with first and last values
first_last(["hello",2,54,-2,7,12,98,"world"])
first_last(["GR",4,554,0,-7,2,-8,8])


'''
#New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your
list first. Then, split your list in half. Push the list created from the first
half to position 0 of the list created from the second half. The output should
be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is
tough!
'''
print '### NEW LIST ###'
def new_list(list):
    # first we sort the list:
    sort_list = sorted(list)
    print sort_list
    # break the list into first and last half:
    first_half = sort_list[:(len(sort_list)/2)] # ':' @ beginning gets stuff before the value
    last_half = sort_list[(len(sort_list)/2):] # ':' @ end gets stuff after the value
    print first_half, last_half
    # build new list with first half incorporated at beginning:
    last_half.insert(0, first_half)
    print last_half
    return last_half
new_list([19,2,54,-2,7,12,98,32,10,-3,6])
new_list([4,20,19,99,-72,2,75,23,60,-4,7])
