# Lists are ordered sequences that can hold a variety of object types.
# In Python lists can be flexible and can hold any type of objects.
my_list = [1,2,3]
new_list = ['string', 100, 10.3]
print (len(new_list))
another_list = my_list + new_list
print(another_list)
# To append a new element to the list we use the append method.
another_list.append('Hello world')
print (another_list)
another_list.pop()
print(another_list)
another_list.remove(100)
print(another_list)
print(another_list.pop(0))
print(another_list)
second_list = [9,6,4,2,1,10]
# The below method will throw an error because sort doesn't have a return type.
#print(second_list.sort)
second_list.sort()
print(second_list)
# Just like sort reverse method also doesn't have a return type, hence the following method will throw an error.
#print(second_list.reverse)
second_list.reverse()
print(second_list)