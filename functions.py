# Creating clean repeatable code is a key part of any development process.
# Fuctions allow us to create blocks of code that can be easily executed many times, without needing of 
# constantly rewriting the entire block of code.
# The syntax of writing a function is as follows
def name_of_function():
    '''
    Docstring explains function
    '''
    print('Hello')

name_of_function()

# Some functions require input and when the input is not passed they throw and error
# To avoid this we can pass a default value

def print_name_function(name = 'Name'):
    '''
    DOCSTRING: Prints name provided
    INPUT: Name
    OUTPUT: Hello Name
    '''
    print('hello {}'.format(name))

print_name_function()
print_name_function('Bob')

def add(n1,n2):
    return n1 + n2

result = add(100,100)
print(result)

def is_prime(n1):
    '''
    DOCSTRING: Returns true if entered value is prime number false otherwise
    INPUT: int
    OUTPUT: True or False
    '''
    for numb in range(2,n1-1):
        print('numb before everything {}'.format(numb))
        if numb < n1 and n1 % numb == 0:
            print(numb)
            return False
            print('numb after true {}'.format(numb))
            break
        elif numb < n1 and numb != n1 -1:
            continue
        elif numb == n1 -1:
            return True

result = is_prime(11)
print(result)