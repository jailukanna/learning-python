# Regular Expressions
"""
Regular expressions, commonly known as regex, are a set of rules for identifying
or matching strings. Many programming languages, including Python, support use of
regular expressions for matching and searching strings.

Common uses include searching string inputs from users. Search engines and other
form input, like user registration and login, are great examples of correct uses
for regular expressions. As you've seen, Django uses regex to match url patterns
in routing. You won't need to do anything too complex when working with Django,
but you can use the following reference for some of the most common expressions
you'll use.

Here is a cheat sheet for expressions you'll be using regularly:
"""

'^'
# Matches the following characters at the beginning of a string. Example: '^a'
# matches 'anna' but not 'banana'.

'$'
# Matches the previous characters at the end of a string. Example: 'a$' matches
# 'anna' and 'banana' but not 'fan'.

'[]'
# Matches any value in a range. Example: '[0-9]' matches '9' and '9s' but not 's9'.

'{n}'
# Matches n number or more repetitions of the preceding pattern. Example: '[0-9]{2}'
# matches '91' and '9834' but not '9'

'\d'
# Matches digits

'\w'
# Matches characters. Example: "\d" matches "8" and "877x" but not "x989"

"""
All of the above examples are pretty simple. You can combine any of the above
patterns to match complex strings. You'll see lots of examples of regex in Django
urls, but they follow a simple pattern.

Use Python's regex documentation as a reference if you need anything more complex
than the above. You most likely won't. If you're curious and you have some spare
time try Regex One to practice your patterns.

Python Regex Documentation: https://docs.python.org/2/library/re.html
"""
