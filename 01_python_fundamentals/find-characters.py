'''
Write a program that takes a list of strings and a string containing a single
character, and prints a new list of all the strings containing that character.

Here's an example:

# input
l = ['hello','world','my','name','is','Anna']
char = 'o'

# output
n = ['hello','world']

Hint: how many loops will you need to complete this task?
Answer: 1
'''

def find_characters(str_list, str_character):
    character = str_character
    character_list = [];
    for word in str_list:
        if character in word:
            character_list.append(word)
    print '#CHARACTER: {}'.format(str_character)
    print '#WORDS: {}'.format(character_list)
    return character_list
    
print '#LIST 1'
find_characters(['hello','world','my','name','is','Anna'], 'o')
print '#LIST 2'
find_characters(['adobe','gimp','corel'], 'e')

'''
Instead of regex, we can use a built in python method that can look at a string
and match for a character or even word.

http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method

example_string = "This is an example string"
substring = "example"
print(substring in example_string)
'''
