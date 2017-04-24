# grab numpy
import numpy as np

# creates an matrix 3x5 in dimensions
# with the values 0-14 in the matrix:
a = np.arange(15).reshape(3, 5)

# print the matrix:
print "/////// MATRIX A ///////"
print a

# print the matrix dimensions:
print "/////// DIMENSIONS OF A ///////"
print a.shape

# prints the number of dimensions (or axises) of the matrix:
print "/////// # OF DIMENSIONS IN A ///////"
print a.ndim

# print number of items in matrix (not index style but actual length):
print "/////// # OF ITEMS IN A ///////"
print a.size

# prints the NumPy type:
print "/////// TYPE OF A ///////"
print type(a)

# create another array:
b = np.array([6, 7, 8])

# prints another array:
print "/////// MATRIX B ///////"
print b

# prints type of matrix b:
print "/////// TYPE OF B ///////"
print type(b)

# prints shape of array b:
print "/////// DIMENSIONS OF B ///////"
print b.shape

# what if you know the dimensions of an array but not the actual values?
# use `zeroes`, `ones` or `empty` to fill in values:

# zeroes placeholder:
c = np.zeros((3,4))
print "/////// NEW MATRIX WITH ZERO PLACE HOLDER ///////"
print c

# ones placeholder:
d = np.ones((2,3,4), dtype=np.int16) # creates 2 matrixes, each 3x4 with 1's as placeholder and datatype as int16
print "/////// NEW MATRIX WITH ONES PLACE HOLDER ///////"
print d

# randomized placeholder (based on memory):
e = np.empty((2,3))
print "/////// NEW MATRIX WITH RANDOM PLACE HOLDER ///////"
print e

# create a sequence from 10 to 30, increasing by 5 and return an array:
# note: final value 30 is never reached - stops at increment beforehand
f = np.arange(10, 30, 5)
print "/////// SEQUENCE TO ARRAY ///////"
print f

# make  a sequence 0 to 2 with floating point numbers, increasing by 0.3 each time and return an array:
# note: final value 2 is never reached - stops at increment beforehand
g = np.arange(0, 2, 0.3)
print "/////// SEQUENCE FLOATING POINT TO ARRAY ///////"
print g
