
"""
Object-Oriented Programming (OOP)
    OOP is a method of structring a program by bundling related properties and behaviours into indivudual objects. 
"""

"""
Define a Class:
    Primitive data structures-like numbers, strings, and lists-are designed to represent simple things, such as the cost of something.
    What if we want to represent something much more complicated?
    A great way to make code more manageable and more maintainable is to use classes. 
"""

"""
Classes vs Instances:
    Classes are used to create user-defined data structures. 
    Classes also have special functions, called methods, that define behaviours and actions that an object created from the class can perform with its data. 

    In this chapter we'll create a Dog class that stores some basic information about a dog. 
    It's important to note that a class just provides structure. 
    A class is a blueprint for how something should be defined. It doesn't actually provide any real content itself. 
    The Dog class may specify that the name and age are necessary for defining a dog, but it will not actually state what a specific dog's name or age is. 

    While the class is the blueprint, an instance is an object built from a class that contains real data. 
    An instance of the Dog class is not a blueprint anymore. It's an actual dog with a name, like Miles, who's four years old. 

    Put another way, a class is like a form of questionnaire. It defines the needed information. 
    After we will out the form, our specific copy is an instance of the class. It contains actual information relevant to us. 

    We can fill out multiple copies of a form to create many different instances, but without the form as a guide, we would be lost, not knowing what information is required. 
    Thus, before we can create individuals instances of an object, we must first specify what is needed by definig a class. 
"""

"""
How to Define a Class:
    All class definitions start with the class keyword, which is followed by the name of the class and a colon. 
    This is similar to the signature of a function, except that we don't need to add any parameters in parentheses. 
    Here is an example of a simple Dog class:
    class Dog:
        pass 
    
    Note: Unlike functions and variables, the convention for naming classes in Python is to use CamelCase notation, starting with a capiltal letter. 
    
    To define the properties, or instance attributes, that all Dog objects must have, we need to define a special method called. __init__().
    This method is run everytime a new Dog object is created and tells Python what the initial state-that is, the initial values of the object's properties-of the object should be. 

    The first positional argument of __init__() is always a variable that references the class instance. This variable is almost universally named self. 
    After the self argument, we can specify any other arguments requried to create an instance of the class. 

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    In the body of the __init__() method, there are two statements using the self variable. 
    The first line, self.name = name, creates an instance attribute called name and assign to it the value of the name variable that was pased to the __init__() method. 
    The second line creates an instance attribute called age and assigns to it the value od the age argument. 

    This might look kind of strange. The self variable is referring to an instance of the Dog class, but we haven't actually created an instance yet. 
    It is a place holder that is used to build the blueprint. Remember, the class is used to define the Dog data structure. It does not actually create any instances of individula dogs with specific names and ages. 

    class Dog:
        # Class Attribute
        species = "Canis familiaris"

        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        We should use class attributes whenever a property should have the same initial value for all instances of a class. 
"""

# Class and Instances Attributes:
class Dog:
    species = "Canias familirias"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.name)
print(miles.age)

"""
    The __init__() method has three parameter, so why are only two arguments passed to it in the example?
    When we instantiete a Dog object, Python creates a new instance and passes it to the first parameter of __init__(). 
     This essentially removes the self parameter, so we ony need to worry about the name and age parameters. 
    After the Dog instances are created, we can access their instances attributes by using dot notation

    Both instances and class attributes can be modified dynamically:
"""
buddy.age = 11
print(buddy.age)

"""
    Recall that an object is mutable if it can be altered dynamically. 
    For example, lists and dictionaries are mutable, but strings and tuples are not-they are immutable.
"""

"""
Instance Methods:
    Instance methods are functions defined inside of a class. This means that they only exist within the context of the object itself and cannot be called without referencing the object. 
    Just like __init__(), the first argument of an instance method is always self:
"""
class Dog:
     def __init__(self,name,age):
            self.name = name
            self.age = age
     def description(self):
             return f"{self.name} is {self.age} years old"
     def speak(self, sound):
            return f"{self.name} says {sound}"

miles = Dog("Miles", 4)

print(miles.description())
print(miles.speak("Woof Woof"))
print(miles)

"""     
    We will some modifying in our code, 
    when we try just print(miles) we take the memory place of object; but with description we can print the miles object. 
    But we can do that more simple way: 
"""
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

buddy = Dog("Buddy", 3)
print(buddy)


