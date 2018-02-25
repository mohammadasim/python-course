# List comprehensions are a unique way of quickly creating a list with python.
# If you find yourself using a for loop along with .append() to create a list, list comprehensions are a good alternative.
# This is the usual approach
my_string = 'Helloworld'
my_list =[]
for letter in my_string:
    my_list.append(letter)
print(my_list)

# with list comprehension we can do it much neatly.
my_string2 = 'Helloworld2'
my_list2 = [letter for letter in my_string2 ]
print(my_list2)
 # The first letter is the return value, I personally read it like this, return letter for letter in the string
 # we can do further checks on the return type
ab_list = [num for num in range(0,11) if num%2==0]
print(ab_list)

# We can do complex calculations using list comprehension.
celcius = [0,10,20,34.5]
farenhite = [((9/5)*temp + 32) for temp in celcius]
print(farenhite)


# We can use if else statements inside list comprehension, but it can lead to code reading problems in the future.
result = [x if x%2 ==0 else 'ODD' for x in range(0,11)]
print(result)

# We can also use list comprehension with nested for loops.
# This is the normal way first
list_1 = [1,3,4,5]
list_2 = [10,100,1000]
result = []
for x in list_1:
    for y in list_2:
        result.append(x*y)
print(result)

# This can be done with list comprehension
new_result = [(x*y) for x in list_1 for y in list_2]
print(new_result)