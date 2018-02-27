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