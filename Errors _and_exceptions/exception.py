# We use three keywords for exception handling
# try: This is the blokc of code to be attempted (may lead to an error)
# except: Block of code will execute in case the is an error in try block
# Finally: A final block of code to be executed, regardless of an error

def add(n1,n2):
    print(n1+n2)

add(10,20)

def new_add(n1,n2):
    try:
        print(n1+n2)
    except:
        print('Looks like you are not adding correctly')

n1 = 10
n2 = 40

new_add(n1,n2)

# Exception with else statement

def minus(n1,n2):
    try:
        print(n1-n2)
    except:
        print("Seems like your input is not correct")
    else:
        print('All your input was correct and you got the restult')

n1 = 30
n2 = 10
minus(n1,n2)
minus('30',10)

def write_file():
    try:
        f = open('test.txt','w')
        f.write('Hey this is my first line')    
    except TypeError as wrong_type:
        print('Wrong_type Error occured')
        print(wrong_type)
    except OSError as wrong_permissions:
        print('Hey you have OS Error')
        print(wrong_permissions)
    finally:
        print("I always run")

write_file()
# To generate the error once you have run the code change th mode of file to r and run it again
# If you don't want to define the type of exception or you don't know what sort of exception will be thrown
# you can simply call the except word as shown in the begining of the example. This way all sorts of exceptions will be handled 
# not the specific exception that we have defined.

def ask_for_int():
    try:
        restult = int(input('Please provide a number: '))
    except ValueError as wrong_input:
        print("Whoops! that is not a number")
    finally:
        print("End of try except finally")

#ask_for_int()

def new_ask_for_input():
    while True:
        try:
            result = int(input('Please provide a number '))
        except ValueError as wrong_input:
            print('Incorrect input provided')
            continue
        else:
            print('Thanks for the correct input')
            break
        finally:
            print('I will alway run')

new_ask_for_input()