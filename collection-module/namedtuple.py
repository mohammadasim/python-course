'''
A namedtuple is almost like a class.  In a normal tuple we can retrieve elements by using the index number
But what if we have created the tuple long time ago or we don't know the index number of
the element.  For this reason we use namedtuple because it gives us the ability to 
name our tuples are then retrieve them based on the names
'''

# Example of normal tuple first
t = (1,2,3,4)
print(t[0])

from collections import namedtuple

# We can consider it like defining a class, as shown below
Dog = namedtuple('Dog', 'age colour breed')

# Once the class has been defined we can instantiate it, as follows

c = Dog(age=2,colour='black',breed='bulldog')

# Now we are getting the vlues of the attributes, it is just like we can do with a class
print(c.age)
print(c.breed)
print(c.colour)
# we can use the index like normal tuple too

print(c[0])
print(c[1])