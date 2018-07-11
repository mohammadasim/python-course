'''
defaultdict is a dictionary like object which provides all methods provided by dictionary but takes first argument
(defualt_factory) as default data type for the dictionary.  Using defaultdict is faster than doing the same using dict.set_default
method.
'''
# A defaultdict will never raise a keyError.  Any key that doesn't exist gets the value returned by the default factory.

from collections import defaultdict

# Let's start with default dictionary
my_dic = {'k':1}
print(my_dic['k']) # 1 is printed as a value of 'k'

# Now if we get the value of k2 which is not in the dictionary we will get keyError

#print(my_dic['k2'])

# Now let's compare it with a defaultdict

my_default_dict = defaultdict(object) # A defaultdict with default factory as object

# Now if we want to get the value of key that doesn't even exist we will get the object

print(my_default_dict['one'])
 # It returns an object, which is its default factory.

for item in my_default_dict:
    print(item)