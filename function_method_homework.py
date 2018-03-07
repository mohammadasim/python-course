# Write a function that computes the volume of a sphere given its radius

def vol(rad):
    return 4/3 * 3.14 * rad**3

print(vol(4))

# Write a function that checks whether a number is in a given range (inclusive of hight and low)

def ran_check(num,low,high):
    return num in range(low,high+1)

print(ran_check(0,1,10))

def ran_strg(num,low,high):
    if num in range(low,high+1):
        return 'In range'
    else:
        return 'Not in range'

print(ran_strg(0,1,10))

# Write a function that calculates the number of upper or lower characters in a string
def up_low(s):
    my_list =list(s.split())
    new_s = ''.join(my_list)
    up = 0
    low = 0
    for char in new_s:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1
        elif not char.isalpha():
            pass
    return 'No. of Upper case characters : {}\nNo. of Lower case characters : {}'.format(up,low)

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

# Write a python function that takes a list and returns a new list with unique elements of the first list

def uniqu_list(l):
    return list(set(l))

print(uniqu_list([1,1,1,2,2,3,3,4,5]))

# Write a function that multiples members of a list and returns the value

def multiply(l):
    result = 1
    for element in l:
        result = result * element
    return result

print(multiply([1,2,3,-4]))

# Write a python function that checks whether a passed string is palindrome or not
def palindrome(s):
    return s == s[::-1]

print(palindrome('madam'))

# Write a function that checks whether a passed string is pangram
import string
def ispangram(str1,alphabet=string.ascii_lowercase):
    
   ''.join(sorted())
   print(str1)


ispangram('a quick brown fox jumps over a lizy dog')