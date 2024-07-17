class Vehicle:
    def __init__(self, color):
        self.color = color 

class Car(Vehicle):
    def __init__(self, color, model):
        super().__init__(color)
        self.model = model 

my_car = Car("Red", "Toyota")
print(my_car.model)

"""
Explanation Summary:
    Vehicle Class: Defines a vehicle with a color. 
    Car Class: Inherits from Vehicle and adds a model attribute. 
    Object Creation: An instance of Car is created with color "Red" and model "Toyota". 
"""

"""
Class Declaration with Inheritance: class Car(Vehicle): defines a class named Car that inherits from the Vehicle class.

Constructor: def __init__(self, color, model): defines the constructor method (__init__). It initializes a new instance of Car.

Calling Superclass Constructor: super().__init__(color) calls the constructor of the superclass Vehicle to initialize the color attribute.

Instance Variable: self.model = model assigns the value of the parameter model to the instance variable self.model.
"""