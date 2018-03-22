class Dog():
# Class Objject Attributes
# These are the same for all instances of a Class
# These are identical to Static attributes in Java
    species = 'mammal'

    # Constructor of the class with three arguments
    # We can provide default values for these attributes and they will be overwritten if the values is provided 
    # at the time of instantiating the object
    # e.g  name = 'Frankie'
    # def __init__(self, breek,name='Frankies',spots)
    def __init__ (self, breed,name,spots):
        self.breed = breed
        self.name = name
        # Expects boolean True/False
        self.spots = spots
        self.short_intro = breed + ' ' + name 

    # Methods of Dog class
    # The main difference between method is Java and Python is the use of self key word
    def bark(self):
        print("WOOF!")
    
    # Using attributes of the class in a method
    # Remember to use the keyword self when referencing attributes of the class
    def introduce(self):
        print('I am {}, my breed if {} and do you think I have spots or not \nI say {} but my species is {}'.format(self.name,self.breed,self.spots,Dog.species))

    # Methods with attributes that are passed to a method
    def affection_to_master(self,master_name):
        print('woof ' + master_name)
my_dog = Dog('lab','Sam',False)
my_dog.bark()
my_dog.introduce()
my_dog.affection_to_master('Donald')
print(my_dog.short_intro)