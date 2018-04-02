class Animal():
    
    def __init__(self):
        print('Animal Created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')
# Now if we wanted to create a Dog class and make it inherit from the animal class, this is how we do it.

class Dog(Animal):
    # In the constructor of Dog we are also initializing the Animal object as well as that is the superclass.
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    def who_am_i(self):
        print("I am a Dog")

    def bark(self):
        print("WOOF")
    






myDog = Dog()
myDog.who_am_i()
myDog.bark()