# A class is always following the camel casing convention
# The __init__() is the constructor of the class. This must always have the key word self in it.
# Unlike Java we don't explicitly declare the variables in the begining of the class
# When assigning the variables in constructor it is imperative to use the self key word

class Dog():

    def __init__(self):
        pass
    


class Cat():

    def __init__(self,name):
        self.name = name

class Person():

    def __init(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    
        
       


my_dog = Dog()
print(my_dog)
my_cat = Cat('miao')
print(my_cat)

my_person = Person()
my_person.age