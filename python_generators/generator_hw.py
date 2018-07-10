'''
Create a generator that generates the squares of numbers up to some number N
'''
def gensquares(N):
    for number in range(N):
        yield number ** 2

#for x in gensquares(10):
    #print(x)

'''
Create a generator that yields 'n' random number between a low and high number that are inputs
'''
import random

def rand_num(low,high,n):
    for number in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)


'''
Use the iter() function to convert the string below to an interator
'''
s = "hello"
it_string = iter(s)

for character in it_string:
    print character

'''
Explain a use case for a generator using a yield statement where you wouldn't want to use a normal function with a return statement:

When generating huge amount to data that is going to be used and then destroyed. It is better to use generator as it will not save anything
in memory.
'''

'''
Generator Comprehension:
It is like list comprehension but instead of finding all the items you are interested and packing them into a list, it waits and yields
each item out of the expresasion one by one
'''
my_list = [1,2,3,4,5,6,7,8,9]
higher_than_three_list = [item for item in my_list if item > 3]
print(higher_than_three_list)
print(len(higher_than_three_list))

# Generator comprehension (the difference is in the style of brackets, for list it is [] for gencomp())

second_list = [1,2,3,4,5,6,7,8,9]
gencomp = (item for item in second_list if item > 3)

#print(gencomp)
#print(len(gencomp)) #so technically it has no length

print(gencomp.next())
print(next(gencomp))