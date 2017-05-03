from django.shortcuts import render
import re # Imports regex module

# Create a list of strings to test against regex patterns for matches:
words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

# Controller Methods:
def index(request):
    """Runs when root route is requested, loads index.html page."""

    print "Running index route!"
    print "Evaluting built-in list of strings..."
    results = {
        "results": __get_matching_words(words)
    }
    # Note: In order for us to attach data to our Template (aka `view`), we must convert our data to a dictionary.
    # If you try and send a list for example, you'll get a Django error.
    return render(request, "searching/index.html", results)

def __get_matching_words(str_list):
    """Checks regex patterns against any strings in a list that is  provided.

    Parameters:
    -str_list: List of strings to check against regex patterns.
    """

    print "Checking strings against regex patterns!"

    # Define regex pattern to test:  
    regex_patterns = re.compile(r'((v|V))|(([s]{2})+([\w]*))|((e$))|(b+.+b)|(aeiou)|^([regularexpression])*$|([a-z])\11')
    """Regex groupings are explained as follows:
    Groupings:
    -#1 `((v|V))` - This grouping matches for either `v` or `V` in a string. Note: This matching only seems to work if both characters are wrapped in a second grouping.
    -#2 `(([s]{2})+([\w*]))` - This grouping (two sub groupings), is first checking for the `s` character in a sequence of {2}, and then also (the `+`) looking for any character (the `\w` indicates a-z, A-Z, 0-9) in any number of repetitions (the, `*` indicates unlimited number of repititions). 
    -#3 `((e$))` - This grouping matches for any string whom ends with `e`.
    -#4 `(b+.+b)` - This grouping matches for any string whom contains the letter `b`, followed by *any* character (letters, numbers, punctuation, etc), and then followed by another `b`. The `.` character indicates "all characters", which includes letters, numbers and basic punctuation characters as afore noted.
    -#5 `(aeiou)` - This grouping matches for the characters `a, e, i, o, u` in a string. The chracters must be in the proper order, otherwise regex will not match the pattern.
    -#6 `^([regularexpression])*$` - This grouping matches for strings which, from start to finish contain only the letters within the word `regularexpression`. Tthe `^` indicates the beginning of the string and the `$` indiciates the end of the string. The `[ ]` indicate a `set`, and to look for the characaters in that set. Again, the `*` indicates that any number of these characters may exist to validate a match. Because of the string restriction (the `^` and `$`), any characters outside of this set will not match.
    -#7 `([a-z])\11` - This grouping matches for any letter, `a-z`, denoted by the `([a-z])` grouping. The `\11` then indicates that the 11th capture group (which is the one containing `[a-z]`), must also exist. This sounds confusing, so to explain in simpler terms. First any character, `a-z` is matched. This character, whatever it is, becomes the `\11` variable, because it is contained within the 11th capture group. (Note: The numbers in these comments do not match exactly the capture groups in the regex pattern, as it was an aim to simplify presentation). In this example, if `b` is found in the first step, then `\11` will also be `b`. The pattern is then evaluating for `bb`. Note that only lowercase letters are examined, and this pattern *will not* catch duplicates such as `Bb` or `Dd`. Nor will it catch `DD`. This could be a place for further modification in the future.

    Although some of these patterns might be improved for even greater accuracy, the above regex pattern should evaluate all words in a given list and match for the various groupings outline dabove.
    """

    # Loop through `str_list` and evaluate each string for regex matches:
    matched_words = [] # list to hold words that pass regex matching
    for string in str_list:
        # if patterns do not match:
        if not regex_patterns.match(string):
            continue
        # if patterns do match:
        else:
            matched_words.append(string)
    # When loop has completed, return new list of matched words.
    print "Returning words which passed regex matching."
    return matched_words     
