# Sets are unordered collections of unique elements.
# Meaning there can only be one representative of the same object
# Set like Maps is represented by {}, however they don't have key:value pair.
my_set = {1,2,3,4,5}
print(type(my_set))
print(my_set)
my_set.add(6)
print(my_set)
print(len(my_set))
my_list = [1,1,1,2,2,2,3,4,5]
# Casting a list into a set
print(set(my_list))