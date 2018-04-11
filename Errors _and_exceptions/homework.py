# Problem 1
# Handle the exception thrown by the code below by using try and except blocks
def square_root():
    for i in ['a','b','c']:
        try:
            print(i**2)
        except TypeError as wrong_list_items:
            print('Wrong list items provided. Please provide either int or floating point')
        finally:
            print('Thanks for using the function')

#square_root()

#Problem 2
# Handle the exception thrown by the code below by using try and except blocks.  Then use a finally block to print 'All Done'

def division_by_zero():
    x = 5
    y = 0
    z = 0
    try:
        z = x/y
    except ZeroDivisionError as divided_by_zero_error:
        print('You are dividing the value by zero')
    finally:
        print('All Done')

#division_by_zero()

# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to 
# account for incorrect inputs.
def ask():
    x = 0
    while True:
        try:
            x = int(input('Input an integer: '))
        except ValueError as wrong_input:
            print('An error occured! Please try again!')
            continue
        else:
            print('Input an integer: {}'.format(x))
            break
        finally:
            print('Thank you, your number squared is: {}'.format(x**2))

ask()    