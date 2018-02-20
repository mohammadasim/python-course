# Solutions for python test
# Numbers are basic data structures. Two types int and floating point. 
# Strings are indexed data structure. Immutable.
# List are ordered collection of elements. Different types of elements can be contained in the same set.
# Tuples are immutable, with limited functinality in python. They are indexed too.
# Dictionaries are un ordered collection of key value pair.
print (((2**5)*10/10)-2+70.25)
#44
print(4*(6+5))
#29
print(4*6+5)
#34
print(4+6*5)
#Floating point number
result = 3+1.5+4
print(type(result))

s = 'hello'
print(s[1])
print(s[::-1])
print(s[4])
print(s[-1])

my_list = 3*[0]
print(my_list)
my_second_list = [0,0,0]

l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
print (l)

L = [5,3,4,6,1]
L.sort()
print(L)

d = {'simple_key':'hello'}
print(d['simple_key'])

e = {'k1':{'k2':'hello'}}
print(e['k1']['k2'])

f = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(f['k1'][0]['nest_key'][1][0])

g = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(g['k1'][2]['k2'][1]['tough'][2][0])

# Dictionaries are not sorted, but there is a special type of dictionary called sortedDictionary.

# Lists are mutable but tuples are immutable.

my_tuple = (1,2,3,4,5)
print(type(my_tuple))

# Sets have only unique elements.

l = [1,2,2,33,4,4,11,22,3,3,2]
print(set(l))

# False
# False
# False
# True
# False
# False
