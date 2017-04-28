import datetime # `datetime` module for call time logging:
import string  # `string` module for generating unique IDs from timestamps (manipulating strings)

# Note: We are using `docstrings` in this document to comment on our classes
# and methods. Docstrings follow a specific convention: They must use triple quotations,
# ie, <""">, along with (1) the first line being a summary, (2) any additional lines
# being in paragraph form with a line break beneath the summary, (3) a line break
# prior to the method/class code. See below for examples. See `/docutilstest.py`
# for how these docstrings can be exported using the built-in `help()` Python method.

class Call(object):
    """Create a call."""

    def __init__(self, name, phone, reason):
        """`Call` constructor method.

        Parameters:
        --name: name of caller (no default setting).
        --phone: phone number of caller (no default setting).
        --reason: reason for calling (no default setting).

        Notes: A timesetamp is automatically added to the Call instance upon
        creation, along with an automatically generated ID.
        """
        self.id = self.__generate_id()
        self.name = name
        self.phone = phone
        self.time = datetime.datetime.now()
        self.reason = reason

    def print_call(self):
        """Prints all details about a call instance."""

        print ">> ID: {}".format(self.id)
        print ">> NAME: {}".format(self.name)
        print ">> PHONE: {}".format(self.phone)
        print ">> TIME: {}".format(self.time)
        print ">> REASON: {}".format(self.reason)
        print "\n"
        return self

    def __generate_id(self):
        """Generates unique ID for Call objects.

        Notes: Unique IDs are generated based upon the timestamp with milliseconds.
        """


        # Note: What's happening here, via chaining, from left to right, is that
        # first we are converting a datetime object of utc now to a string (rather
        # than a datetime object type). Once in string form, we can tap into
        # the 'string' module. We use `translate()` with `string.punctuation` as
        # a parameter to remove any punctuation from the timestamp (such as dashes
        # or colons). Once we've removed all punctuation, we finally call upon
        # the `replace()` function to remove any whitespace (the " ")[quotations
        # with a space between them] and convert it to none (the "")[quotations
        # without a space between them]. This guarantees that each number is
        # unique, as its based off of the complete date (year, month, day, hour,
        # second, and millisecond). No two timestamps should ever be the same.
        # Note: You could probably use Regex here instead somehow to remove
        # all of the punctuation and spaces.
        unique_id = str(datetime.datetime.utcnow()).translate(None, string.punctuation).replace(" ", "")
        # print unique_id, "<<<<<"
        return unique_id

class Call_Center(object):
    """Manages Call objects."""

    def __init__(self):
        """'Call Center' constructor method.

        Notes: Contains `calls` property which contains list of all call objects,
        as well as `queue_size`, which gives the length of the call list.
        """

        self.calls = [] # holds call objects
        self.queue_size = len(self.calls) # returns # of calls
        return None

    def add(self, call):
        """Adds call to call center queue.

        Parameters:
        --call: call to add to `calls` list (no default setting).
        """

        self.calls.append(call) # add call to `calls` list
        self.queue_size = len(self.calls) # update `queue_size`
        return self

    def remove(self):
        """Removes call from front of `calls` queue."""

        del self.calls[0] # removes 0 index from calls queue
        self.queue_size = len(self.calls) # update queue
        return self

    def info(self):
        """Displays name, phone number of each call and total length of queue."""

        print "=========== CALL QUEUE ============"
        for call in self.calls: # loop through calls:
            print ">> CALL #: {}".format(self.calls.index(call))
            print ">> CALL ID: {}".format(call.id)
            print ">> NAME: {}".format(call.name)
            print ">> PHONE: {}".format(call.phone)
            print "\n"

        if not self.calls: # if queue is empty:
            print 'CALL QUEUE IS EMPTY.'
        print "\n", "********** TOTAL **********"
        print "* {}".format(self.queue_size)
        print "***************************"
        print "============ END QUEUE ============"
        print "\n"
        return self

# Testing Instances of our Call class Objects:
print "#-------------#   T E S T I N G  `C A L L`  C L A S S E S   #-------------#"
call1 = Call('Tim Knab', '206-271-1443', 'I\'v fallen and I can\'t get up.')
call2 = Call('Mit Bank', '344-117-2602', 'I\'v gotten up and I can\'t fall.')
call3 = Call('T K', '000-000-0000', 'I\'v gotten up and I can\'t fall.')
call4 = Call('M B', '111-111-1111', 'I\'v gotten up and I can\'t fall.')

# Testing Call class Object Instance Methods:
call1.print_call()
call2.print_call()
call3.print_call()
call4.print_call()

print "\n"
print "#-------------#   T E S T I N G  `C A L L   C E N T E R`   #-------------#"
call_center = Call_Center()
# print "CALLS:", call_center.calls
# print "QUEUE SIZE:", call_center.queue_size

# Testing adding some Calls:
call_center.add(call1)
# print call_center.calls
# print call_center.queue_size
call_center.info()
call_center.remove()
call_center.info()

# Testing chaining some additions and removals:
call_center.add(call1).add(call2).add(call3).add(call4).remove().info()
