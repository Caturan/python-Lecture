
# Parent Classes vs Child Classes

# Let's create a child class for each of three breeds: Jack Russel Terrier, Dachshund and Bulldog. 

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Remember, to create a child class, we create new class with its otwn name and then put the name of the parent class in parantheses. 

class JackRusselTerrier(Dog):
    pass 

class Dachshund(Dog):
    pass 

class Bulldog(Dog):
    pass 

# With the child classes defined, we can now instantiate some dogs of specific breeds:

miles = JackRusselTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

# To determine which class a given object belongs to, we can use the built-in type() function:
print(type(miles))

# What if we wanted to determine if miles is also an instance of the Dog class? We can do this with the built-in isintance() function:
print(isinstance(miles, Dog))
# Notice that isinstance() takes two arguments, an object and a class. 
print(isinstance(miles, Bulldog))
print(isinstance(miles,JackRusselTerrier))
# More generally, all objects created from a child class are instances of the parent class, although they may not be instances of other child classes. 


"""
Extending Functionality of a Parent Class
    Since different breeds of dogs have slightly different barks, we want to provide a default value for the sound argument of their respective .speak() methods. 
    To do this, we need to override the .speak() method in the class definition each breed. 
    To override a method defined on the parent class, we define a method with the same name on the child class. 
"""
class JackRusselTerrier(Dog):
    def speak(self, sound="Hrr"):
        return f"{self.name} says {sound}"

miles = JackRusselTerrier("Miles", 4)
print(miles.speak())
# We can still call .speak() with a different sound

# One advantage of class inheritance is that changes to the parent class will automatically to their child classes. 

""" 
    We can access the parent class from inside a method of a child class by using the super() function. 
    
    In many real world examples, the class hierarchy can get quite complicated with one class inheriting from a parent class, 
     which inherits from another parent class, which inherits from another parent class, and so on. 

    The super() function does much more than just search the parent class for a method or an attribute. 
     It traverses the entire class hierarchy for a matching method or attribute. If we aren't careful, super() can have surprising results. 
"""

