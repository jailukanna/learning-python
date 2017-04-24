'''

Optional Assignment: The Requests Library
Build a simple program that makes use of the requests module.

In addition to including a lot of great features in the language itself, there
are many modules available for install via pip that are a lot of fun to work
with. We talked a little about pip before, so you should have the basic idea
that pip exists so that developers can use code other people have written.

One of those code libraries is called requests. It allows you to make HTTP
requests from a python file and get back a useful response. This library is a
simple way to make requests to and get responses from a server without having
to set one up yourself. This might remind you a little of using AJAX to interact
with API's like you did in web fundamentals. Give it a try and get creative with
the data you try to get back.

Link for How to Install `Requests`:
http://docs.python-requests.org/en/master/user/install/#install

Link for how to create a Virtual Environment:
https://docs.python.org/3/library/venv.html
http://docs.python-guide.org/en/latest/dev/virtualenvs/
'''

# get requests library:
import requests

# build user input so user can choose a pokemon to retrieve via `requests` library
number = input("Enter a number of a Pokemon between 1 and 151:")

# user input validations:
    '''
    Note: This valiation could be improved by checking if `number` is String.
    For simplicity right now this program assumes it's a Integer.
    '''
if number >= 152:
    number = input("Number too large. Choose a number between 1 and 151:")

if number < 1:
    number = input("Number too small. Choose a number between 1 and 151:")

# build request URL based on user input and validations (get Pokemon):
r = requests.get("http://pokeapi.co/api/v2/pokemon/" + str(number))

# prints JSON data:
# print r.json()

print "\n"
# Print information about the key values:
print "~~~~~~~ BEGIN POKEMON DATA KEY VALUES ~~~~~~"
# Set pokemon to returned data as JSON:
pokemon = r.json()
# Iterate over JSON keys to see what we can view from this Pokemon:
for item in pokemon:
    print item
print "~~~~~~~~ END POKEMON KEYS ~~~~~~~"

print "\n"
# Print information about the Pokemon
print "=================================="
print "======= YOUR POKEMON DATA ========"
print "=================================="
print "Pokemon name: {}".format(pokemon['name'])
print "Pokemon weight: {} pounds".format(pokemon['weight'])
print "Pokemon height: {} feet".format(pokemon['height'])
print "\n"
# iterate over pokemon abilities keys (unpack the data):
print "Pokemon abilities:"
for ability_info in pokemon['abilities']:
    print "- {}".format(ability_info['ability']['name'])
print "\n"
# iterate over pokemon stats keys (unpack the data):
print "Pokemon stats:"
for stat_info in pokemon['stats']:
    print "- {}: {}".format(stat_info['stat']['name'], stat_info['base_stat'])
