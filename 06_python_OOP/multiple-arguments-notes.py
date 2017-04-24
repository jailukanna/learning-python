# the `*` is a splat operator, and lets you pass along a variable number of arguments
# the splat operator bundles the remaining arguments into a tuple
# you'll see below that varargs() can take 1, or infinite arguments
# the .join() method joins the values in the tuple together
def varargs(arg1, *restOfArg):
	print "Got " + arg1 + " and " + ", ".join(restOfArg)

# thus if we invoke our methods:

varargs('one')
# prints 'Got one and '
varargs('one', 'two')
# prints 'Got one and two'
varargs('one', 'two', 'three')
# prints 'Got one and two, three'

# the join method above allows whatever arguments added to be stuck together 

# if we tried to test the type of `restOfArg` using:
type(restOfArg)

# this would be returned:
def varargs(arg1, *restOfArg):
	print "restOfArg is of " + str(type(restOfArg))
	varargs("one", "two", "three")
	restOfArg is of <type 'tuple'>
