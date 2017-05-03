# Optional Assignment: Simple Searching

Starting with the code snippet below, write a regex that will match:

+ All words that contain a “v”
+ All words that contain a double-“s”
+ All words that end with an “e” 
+ All words that contain an “b”, any character, then another “b” 
+ All words that contain an “b”, at least one character, then another “b” 
+ All words that contain an “b”, any number of characters (including zero), then another “b” 
+ All words that include all five vowels in order 
+ All words that only use the letters in “regular expression” (each letter can appear any number of times) 
+ All words that contain a double letter

`
import re # imports regex module

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
	matches = []
	for word in words:
 		if re.search(regex,word):
 			matches.append(word)
	return matches
`

For this assignment, you might find an online regex tester, such as Pythex), to be helpful.

Feel free to play around with more regex beyond this!
