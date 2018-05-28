'''
We have learned how to cerate functions with def and the return statement. Generator functions allow us to write a 
function that can send back a value and then later resume to pick up where it left off.
This type of function is a generator in Python, allowing us to generate a sequence of values over time.
The main difference in syntax will be the use of a yield statement.
When a generator function is compiled they become an object that supports an iteration protocol.
That means when they are called in your code they don't actually return a value and then exit.
Instead generator function will automatically suspend and resume their execution and state around the last point
of value generation.
The advantage is that instead of having to compute an entire series of values up front, the generator computes
one value waits until the next value is called for.
For example the range() function doesn't produce a list in memory of all the values from stat to stop, instead
it just keeps track of the last number and the step size to provide a flow of numbers.
If the user did need the list, they have to transform the generator to a list with list(range(0,10))
'''
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(n**3)
    return result
    

print(create_cubes(10))

'''
The above function can be transformed into a generator in the following way.
'''

def create_cubes_gen(n):
    for x in range(n):
        yield x**3

for kube in create_cubes_gen(10):
    print(kube)


def gen_fibon(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        # This part of the calculation is for creating the fibon and the next step.
        a,b = b, a+b 

'''
Important point to note is that in order to print the output of generator
we have to iterate through it using a for loop.
'''

for number in gen_fibon(10):
    print(number)

def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))

'''
As you can see that an error is being thrown, as we try to get the next generator using next() method.
In for loop behind the back this error is thrown and cuaght and we don't know about it.
'''

s = 'hello'
for letter in s:
    print(letter)
#next(s)

# The above method will throw error as string is not iterable. But we can can change it to interable

s_iter = iter(s)
print(next(s_iter))