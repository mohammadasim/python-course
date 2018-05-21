'''
Decorators is an advance python topic. Decorators allow you to decotate a function. Suppose we have a function and we want to add 
extra functionality to it.  There are two options first is to add extra code to the existing function, the problem is that as we have
modified the old function its functionality has changed and hence we can't call is easily.
Another option is to create a new function copy the code from the previous function and then add new code to it, but it means 
we had to rewrite the code, even though it is simple copy and paste.
But what if we then want to remove that extra functionality. We would need to delete it manually or make sure to have the old function
A better way is to have an on/off switch to quickly add this functionality.
Python has decorators that allow us to tack on extra functionality to an already existing function.
We use the @ operator and are then placed on top of the original function.
'''
def func():
    return 1
    
#print(type(func))
#print(func)

def hello():
    return "Hello!"

greet = hello

#print(greet)
#print(greet())
#del hello
#hello()
'''
Important point to note is that functions are objects that can be passed to another object.
Above we deleted the hello() function but we can still execute the greet as a function, because hello() 
function was passed on to it.
'''
#print(greet())

def hello(name='Asim'):
    print('The hello function has been executed!')

    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t this is welcome() inside hello'
    
    print('I am going to return a function!!')

    if name == 'Asim':
        return greet
    else:
        return welcome
'''
Important point to notice is that greet() and welcome functions are only visible inside the hello() function.
Outside these functions these functions are not visible. so how can we access these functions.  Well if we can make 
hello() to return a function then it will work. So the hello() function will be modified to return the greet or welcome function 
rather then just using the print statement.
'''
#my_new_func = hello()
#print(my_new_func)
#print(my_new_func())

def cool():
    def super_cool():
        return 'I am very cool!!'
    return super_cool

#some_func = cool()
#print(some_func())


def hello():
    return 'Hi Asim'

def other(some_def_func):
    '''
    Unlike before now we are passing function as an agrument
    we then execute some code and then exectue the function 
    passed as an argument.
    '''
    print('Other code runs here!')
    print(some_def_func())

# It is important to notice that we are passing hello not hello(), because hello() is execution and 
# we don't want to execute the function, the execution will be done inside the other()
print(other(hello))


def new_decorator(original_func):

    def wrap_func():
        '''
        The idea is to take a function, add extra functionality to it and then return it
        All the above examples are to prepare for the decorator and to understand it better.
        '''
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function!')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!!')
'''
 Below is the long way of doing things. 
'''
#decorated_func = new_decorator(func_needs_decorator)
#print(decorated_func())

'''
The shortest way is as follows
'''
@new_decorator
def func_needs_decorator():
    '''
    This decorator at the top acts like a switch, if it is active the extra functionality is added
    to the function, if it is commented off or removed the extra functionaltiy is removed.
    '''
    print('I want to be decorated!!')

print(func_needs_decorator())
