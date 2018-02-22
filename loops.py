my_list = range(10)
for numb in my_list:
    if numb > 0 and numb%2 == 0:
        print(numb)

my_string = "To Whom it may concern"
for letter in my_string:
    print(letter)


my_dic = {'key1':'lamb','key2':'Beef','key3':'chicken'}
keys = my_dic.keys()
for each_key in keys:
    print(my_dic[each_key])


# Tuple unpacking is common thing in python. Where data return type from a function is of type tuple
# This return type is then unpacked as shown below.

tuple_list = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for a,b in tuple_list:
    print(a)
    print(b)

print('Another example')

mylist = [(1,2,3),(4,5,6),(7,8,9),('a','b','c')]
for a,b,c in mylist:
    print(b)