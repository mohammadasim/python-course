# Generators are functions that generate data without keeping it in memory.
# The range() function is a generator.

index_count = 0
for letter in 'abcde':
    print ('The index for the letter {} is {}'.format(letter, index_count))
    index_count += 1

# To accomplish the above python has a builtin function that removes the need for us maintaining our own index count
word = 'abcde'
for index,letter in enumerate(word):
    print(index,letter)

# You can get them as tuples also

for item in enumerate(word):
    print(item)


# Zip 