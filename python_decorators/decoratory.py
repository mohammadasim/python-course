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
    
    print(greet())
    print(welcome())
    print('This is the end of hello function')
'''
Important point to notice is that greet() and welcome functions are only visible inside the hello() function.
Outside these functions these functions are not visible. so how can we access these functions.  Well if we can make 
hello() to return a function then it will work. So the hello() function will be modified to return the greet or welcome function 
rather then just using the print statement.
'''
print(hello())