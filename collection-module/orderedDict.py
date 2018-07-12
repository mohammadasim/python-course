'''
Ordered dictionary is a sub class of collection module, whick keeps the order in which key-value 
pairs were added to it. In an ordered dictionary two dictionaries are equal only if the order of
their key-value pair is identical also with keys and values
'''
# Lets consider normal dictionary first:

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for kv in d.items():
    print(kv)

# As shown above a normal dictionary doesn't really care about the order of key-value pairs

c = {}
c['a'] = 1
c['b'] = 2
c['e'] = 5
c['d'] = 4
c['c'] = 3

print(d == c)
 # Now lets consider ordered dictionary
from collections import OrderedDict
a = OrderedDict()
a['a'] = 1
a['b'] = 2
a['c'] = 3
a['d'] = 4
a['e'] = 5

for kv in a.items():
    print(kv)
    # As the print output has shown ordered dict does care about the order of the key-value pair

b = OrderedDict()
b['a'] = 1
b['c'] = 3
b['b'] = 2
b['c'] = 4
b['d'] = 5

print(a == b)
# The result if false because the order of the dictionary is different