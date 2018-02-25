# Use for, split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)
# Use range() to print all the even numbers from 0 to 10.
for num in range(1,11):
    if num%2 == 0:
        print(num)
# Correct answer
result = list(range(0,11,2))
print(result)

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
my_list = [num for num in range(1,51) if num%3 == 0]
print(my_list)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word)
        print('even!')

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for numb in range(1,101):
    if numb%3 == 0 and numb%5 == 0:
        print('fizzBuzz')
    elif numb % 3 == 0:
        print('Fizz')
    elif numb % 5 == 0:
        print('Buzz')
    else:
        print(numb)
        
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
result = [x[0] for x in st.split()]
print(result)