# Dictionaries are unordered mappings for storing objects.  
# The key-value pair allows users to quickly grab objects without needing to know an index location.
# Dictionary uses {} and colons to signify the keys and their associated values.
my_dic = {'key1':'value', 'key2':'value2'}
print (my_dic)
print (my_dic['key1'])

my_other_dic = {2:3,4:5}
print(my_other_dic[2])

# Dictionary like list are flexible with holding elements, they can be string, int, float, list or even other dictionaries.

d = {'k1':100, 'k2':200}
d['k3'] = 300
print (d)