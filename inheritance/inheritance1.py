# Python Inheritance
"""
Inheritance allows us to define a class that inherits all the methods and properties from another class. 
Parent class : is the class being inherited from, also called base class. 
Child class : is the class that inherits from another class, also called derived class. 
"""

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:

# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fnmae, lname):
        self.firstname = fnmae
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Use the Person class to create an object, and then execute the printname method:
x = Person("Jack", "Shepard")
x.printname()


# Create a Child Class
"""
To create a class that inherits the functionality from another class, 
send the parent class as a parameter when creating the child class:
"""
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    pass

# Use the pass keyword when we do not want to add any other properties or methods to the class. 

# Use the Student class to create an object, and then execute the printname method:
x = Student("Kate", "Austen")
x.printname()

"""
When we add the __init__() function, the child class will no longer inherit the parent's __init__() function. 
The child's __init__() function overrides the inheritance of the parent's __init__() function. 
"""
class Student(Person):
    def __init__(self, fnmae, lname):
        Person.__init__(self, fnmae, lname)


# Use the super() Function
"""
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
"""
class Student(Person):
    def __init__(self, fnmae, lname):
        super().__init__(fnmae, lname)

"""
By using the super() function, we do not have to use the name of the parent,
it will automatically inherit the methods and properties from its parent.  
"""
class Student(Person):
    def __init__(self, fnmae, lname):
        super().__init__(fnmae, lname)
        self.graduationyear = 2019


class Student(Person):
    def __init__(self, fnmae, lname, year):
        super().__init__(fnmae, lname)
        self.graduationyear = year

    def printobject(self):
        print(self.firstname, self.lastname, self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printobject()
"""
In this example, the year 2019 should be a variable, and passed into the Student class when creating student objects. 
To do so, add another parameter in the __init__() function. 
"""


# Add a method called welcome to the Student class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Elizabeth","Olsen", 2020)
x.welcome()
"""
If we add a method in the child class with the same name as a function in the parent class,
the inheritance of the parent method will be overridden. 
"""

