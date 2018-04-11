# Pylint is a library that looks at your code and reports back possible issues
# Install pylint using pip, pip install pylint in the virtualenv
# It is very important that we include a multi line comment in the begining of every function
# We also shouldn't use a single character as a variable name
'''
A very simple script
'''
def myfunc():
    '''
    A simple function
    '''
    first = 1
    second = 2
    print(first)
    print(second)
    