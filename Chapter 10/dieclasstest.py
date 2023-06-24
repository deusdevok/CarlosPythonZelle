# This file is to learn about classes

from random import randrange

class MSDie:
    # Each function inside a class is called a method
    
    def __init__(self, sides):
        # The special method __init__ is the object constructor, used to initialize a new MSDie
        # This method provides initial values for the instance variables

        # self (first parameter) contains a reference 
        # to the object on which the method is acting
        
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides+1)

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

# Each instance of a class has its own instance variables
die1 = MSDie(6)
print('die object', die1)
print(die1.getValue())
die1.setValue(8)
print(die1.getValue())