# pylint: disable=print-statement
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

# If we want to get part of a string starting a particular index, we use the following syntax
string = 'abcdefghj'
print(string[2:])

# If we want to get part of a string starting from the begining and till index 4, then we use the following syntax. 
# Please note that it is till index 4 but not including index 4.
print(string[:4])

# Combining the above the above, if we want to grab 'def' from the above string, we will use the following syntax.
print(string[3:6])

# If we want to print a string with a jump of two then we can do it with the following syntax. So in the following it starts
# from a and after that rather than going to b it goes to c and continues like this.
# if we want 3 we can replace 2 with 3.
print(string [::2])

# In the following syntax we want a subsection of string starting from 2 till 6 but not including 6 and we want the jump to be 2.
print(string[3:6:2])

#############################  String Properties ####################################
# Just like java string in python is immutable
x = 'Hello world'
x = x + ' it is beautiful outside.'
print (x)

# To get multiple cancatenation we use the following sytax.
y = 'z'
print (y * 10)

b = 'hello world'
b = b.capitalize()
b = b.upper()
print (b)