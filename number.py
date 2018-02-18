# pylint: disable=print-statement
from __future__ import division
# The above line will import the python 3 module and it will enable true division in python 2.
print(3*2)
print(3/2)
# If we don't import division from the above future module then the above line will give us result 1 in python 2.
print(float(3)/2)
#In python 2 in order to achieve real division we have to either import the division module like above, cast 1 of the numbers
# into float like above or simply make 1 of the numbers floating point number.
print 3/2.0
print 2**3

# % it is the mod operator that gives us the reminder in a division operation.  This can be used to check if a number is 
# even or odd.

print 7%3

# To get 2 to the power of 3 we can use the following.

print 2**3