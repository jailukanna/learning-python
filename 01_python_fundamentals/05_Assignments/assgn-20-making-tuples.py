'''
Write a function that takes in a dictionary and returns a list of tuples where
the first tuple item is the key and the second is the value. Here's an example:

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
'''


def make_tuples(dictionary):
    # print dictionary
    output = []

    for value in dictionary:
        # print value
        # print dictionary[value]
        output.append((value, dictionary[value]))
    print output
    return output


make_tuples({"Speros": "(555) 555-5555", "Michael": "(999) 999-9999", "Jay": "(777) 777-7777"})
make_tuples({"Tim": "(111) 111-1111", "Julianna": "(222) 222-2222", "Billy": "(333) 333-3333"})
