# Generators are functions that generate data without keeping it in memory.
# The range() function is a generator.

index_count = 0
for letter in 'abcde':
    print ('The index for the letter {} is {}'.format(letter, index_count))
    index_count += 1

# To accomplish the above python has a builtin function that removes the need for us maintaining our own index count
word = 'abcde'
for index,letter in enumerate(word):
    print(index,letter)

# You can get them as tuples also

for item in enumerate(word):
    print(item)


# Zip is used to combine lists as tuples in a single list. 
# If 1 list is longger than the other the zip will go as far as the shortest list and will ignore the rest of the element of 
# of the long list.
print('Following is the result of zip')
list_1 = [1,2,3,4,5]
list_a = ['x','y','z']
for item in zip(list_1,list_a):
    print (item)

# You can cast the result of zip into a list
print(list(zip(list_1,list_a)))

# 'in' is a key word that is used to check if the presence of an element in an interable object i-e string list, or even dictionary.
# we are already using it in for loop.
print('a' in 'abcd')
print(1 in [8,9,7])
d = {'k1':'v1','k2':'v2','k3':'v3'}
print('k1' in d.keys())
print('v8' in d.values())

# min() and max() functions in python returns the minimum and maximum values of a list respectively.
print(min([1,2,3,45]))
print(max([1,2,3,45]))

# Python comes with a random library. we have to import this library
from random import shuffle
new_list = [1,2,3,4,6,7,5,8,9,10]
shuffle(new_list)
print(new_list)
from random import randint
print(randint(1,1000000))

# How to accept user input
name = input('What is your name: ')
print('hello {}'.format(name))