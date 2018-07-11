'''
Counter is a subclass of the dict used for counting hashable objects. All of python's immutable built-in object are hashable;
mutable containers such as lists or dictionaries are not.  It is an unordered collection where elements are stored as 
dictionary keys and their count are stored as dictionary values. Counts are allowed to be any integer values including
0 and negative counts.
'''

'''
An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() or __cmp__() method). Hashable objects which compare equal must have the same hash value.
'''

from collections import Counter

l = [1,1,1,11,2,2,2,2,3,3,3,3,4,4,4,4,4]
print(Counter(l))

s = "sssswerewkjllkkljdfklsdjflajlkdsjfal"
print(Counter(s))

# If we want to count the number of words in a sentence we have to do the following

sen = 'Hello hello hellow how are you you you doing today'
sentence = sen.split(" ")
print(Counter(sentence))

c = Counter(sentence)

print(c.values())

