# Lesser of two evens: write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd.

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0 :
        return min(a,b)
    else:
        return max(a,b)

print (lesser_of_two_evens(5,3))

# Animal crackers: Write a function that takes two-word string and return True if both words begin with same letter

def animal_crackers(text):
    process = text.lower().split()
    return process[0][0] == process[1][0]

print(animal_crackers('Horse rabbit'))

# Makes twenty: Given tow integers, return True if the sum of the integers is 20 or if one of the integers is 20
# if not return False

def makes_twenty(n1,n2):
    return ((n1+n2) == 20 or n1 == 20 or n2 == 20)

print(makes_twenty(2,10))


# Write a funciton that capitalizess the first and fourth letters of a name
def old_macdonald(name):
    first_letter = name[0]
    till_forth = name[1:3]
    forth_letter = name[3]
    reminder = name[4:]
    return first_letter.upper() + till_forth + forth_letter.upper() + reminder
print(old_macdonald('macdonald'))


# Given a sentence with the words reversed
def master_yoda(text):
    input = text.split()
    length = len(input)
    result = ""
    while length != 0:
        result = result + " " + input[length -1]
        length -= 1
    return result

# Better version of the above method.
def master_oda(text):
    input_list = text.split()
    input_list.reverse()
    return ' '.join(input_list)


print(master_yoda('I am home'))
print(master_oda('I am at work'))

print(abs(100 - 5))


def has_33(nums):
    first_occurance = nums.index(3)
    return nums[first_occurance +1] == 3

print(has_33([1,3,1,3]))

def blackjack(a,b,c):
    if a+b+c <= 21:
        return a+b+c
    elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:
        return a+b+c
    else:
        return 'BUST'

print(blackjack(5,6,7))
print(blackjack(9,9,9))

def summer_69(arr):
    result = 0
    if 6 in arr:
        index_of_6 = arr.index(6)
        index_of_9 = arr.index(9)
        trimmed_array_1 = arr[:index_of_6]
        trimmed_array_2 = arr[index_of_9+1:]
        result = sum(trimmed_array_1) + sum(trimmed_array_2)
    else:
        result = sum(arr)
    return result
print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))