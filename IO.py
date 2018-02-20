# If the textfile doesn't exist or the path to the file is incorrect then the following function will throw an error.
my_file = open('test.txt')
my_file.read
my_file.seek(0)
file_content = my_file.read()
print(file_content)
# After the read command above the cursor is now at the end of the file and hence a nother read command will return empty string.
# To move the cursor back to the begining we use the following command.
my_file.seek(0)
readline_content = my_file.readline()
print(type(readline_content))
print(readline_content)
my_file.seek(0)

readlines_content = my_file.readlines()
print(type(readlines_content))
print(readlines_content)

# As best practice it is important to close the file. If we will forget to close the file we will get error if we
# wanted to delte the file etc as this file will be in use in python.
my_file.close()

# To avoid the above problems the best solution is to open the file as follows.
with open('test.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)

with open('test.txt', mode='w') as my_test_file:
    my_test_file.write('Hey this is the new file I am writing on to the file.')

with open('test.txt', mode='a') as append_test_file:
    append_test_file.write('\nThis is the second line.\nThis is the third line.\nThis is the forth line.')

# To write a totally new file we can do as follows.
with open('example.txt', mode='w') as new_file:
    new_file.write('Hello this is the new file I just created.')