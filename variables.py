# Python is dynamically typed, it means that we can assign any type of value to a variable.
# Unlike Java which is statically typed. Which means we have to declare the type of the variable and can only
# assign that type of value to it.
a = 5
print a
a = a + a

print a

a = 'b'
# We can use the type function to determine the type of the variable a in the following example.
# We will get string as a currently have the value 'b'. If however we will change it to an int then the type() function
# will return the type as int
print type (a)

my_income = 100
my_tax_rate = 0.40
my_tax = my_income * my_tax_rate
print my_tax