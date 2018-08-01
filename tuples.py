# Tuples are very similar to list.
# Unlike list tuple are immutable.
t = (1,2,3,'one')
l = [1,2,3,4]
print (type(t))
print (type(l))
print(t[1])

my_tuple = (1,1,1,2,3,4,5)
print(my_tuple.count(1))
print(my_tuple.index(1))
print(my_tuple.index(2))
'''
We can not append anything to a tuple but we can change a tuple as shown below.
'''
t = t +('two',)  # remember to always put the comma at the end otherwise it will not work.
print(t)

# to create a single value tuple the following is the code.
unit_tuple = (15,) #Don't forget to use the , otherwise python will not recognize it as a tuple.