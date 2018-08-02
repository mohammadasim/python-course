# They are anonymous functions.
# Map function takes a function and apply it over the entire iterable.
# When passing function to map, we pass it as an argument and not execute it inside the map function
# Execution of the function is done by the map function.
def square(number):
    return number**2

my_num = [1,2,3,4,5,6]

for item in map(square, my_num):
    print(item)

print(list(map(square, my_num)))


# Filter applies a check on to a list of iterables
# With filter we have to pass a function that does the check and we need to surround the filter with a list too.

def check_even(num):
    return num % 2 == 0

print(list(filter(check_even, my_num)))

# Lamda functions are anonymous functions that can be used only once
# In the above example we had first create a function to check even number and then use it with filter to apply to a list
# we can easily replace this function with a lamda function.
# as a first step we bring the return type on the same line
# def check_even(num): return num % 2 == 0

# the next step is to remove the return word
# def check_even(num): num % 2 == 0

# Since lamda functions are anonymous we have to get rid of def and check_even
lambda num :num % 2 == 0

# we can use the above with filter function like before
print(list(filter(lambda num: num % 2 == 0, my_num)))

# we can do the same with the map function done above
print(list(map(lambda x: x **2, my_num)))