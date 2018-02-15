# In Python strings are represented by either single quote or double quote.
# If we are having a single quote in our string and we want to keep that, the we must use double quote.
my_string = "Hello"
print my_string
print my_string[0]
print my_string[3]

# In Python there is reverse indexing. If we want to grab the last character of a string, but we don't know the length
# of the string, then all we have to do is use -1 for the index of the last character. Similarly the second last
# will be -2 and it continues like this.  This is called reverse indexing.

print my_string[-1]

# We can easily reverse a string by using the syntax [::-1], this states to give all the indexes starting from -1, i-e
# the last character in the string.
print my_string[::-1]

print len(my_string)

# We can use special escape characters in python, For example \n can be used to tell python we want a new line, as hown bellow.
another_string = "I'm going on a run. \nBut it is raining my buddy said."
print another_string