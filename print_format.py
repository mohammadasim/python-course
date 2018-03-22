# pylint: disable=print-statement
from __future__ import print_function
# Formatting with the .format() method
# A good way to format objects into your strings for print statement is with the string .format() method. The syntax is 
# 'String here {} then also {}'.format('something1';'something2')
print ('This is a string {}'.format('INSERTED'))
print ('The {} {} {}'.format ('fox','brown','quick'))
print ('The {2} {1} {0}'.format ('fox','brown','quick'))
print ('The {q} {b} {f}'.format (f='fox', q='quick', b='brown'))

# Float formatting follows "{value:width.percision f}"
# width is the width of the value, if increased it adds white space to the value.
result = 100/777.0
print (result)
print ('1. The result is {}'.format(result))
print ('2. The result is {r}'.format(r=result))
print ('3. The result is {r:1.3f}'.format(r=result))
print ('4. The result is {r:8.3f}'.format(r=result))

# Formatted literals are represented by f.  This is new edition to python.  It is addition to python 3.6 hence will not work 
# in the older version of python.
name = 'Adam'
#print (f'His name is {name}')