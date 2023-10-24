
# Function names should be lowercase, with words seperated by underscores as necessary to improve the readability. 

# Basic function definition:
def function_name():
    pass

# Input and Output Arguments:
def fn(arg1, arg2):
    return arg1 + arg2


# Default values for arguments:
def fn(arg1 = 0, arg2 = 0):
    return arg1 + arg2

print(fn())


# Type Hints and Default Values for arguments:
def fn(arg1: int = 0, arg2: int = 0) -> int:
    return arg1 + arg2

print(fn())

# Lambda Functions:
fn = lambda arg1, arg2: arg1 + arg2

print(fn(5, 6))

# Function Docstrings: One-line Docstrings
def fn(arg1 = 0, arg2 = 0):
    """This function sums two number."""
    return arg1 + arg2

print(fn())


# Multi-line Docstrings
def fn(arg1 = 0, arg2 = 0):
    """This function sums two number.

    Keyword arguments:
    arg1 -- first number (default 0)
    arg2 -- second number (default 0)
    Return: the sum of arg1 and arg2
    """
    return arg1 + arg2



    """
    In python, function parameters can be categorized into two main types:     
    positional parameters and keyword parameters(also known as keyword arguments)
    """


# Positional Parameters:
def add(a, b):
    return a + b

result = add(2, 3) # Here, 2 is matched to 'a', and 3 is matched to 'b'
    

# Keyword parameters(Keyword Arguments)
def greet(name, message = "Hello"):
    return f"{message}, {name}"

greeting = greet(name="Alice", message="Hi") # Using keyword arguments

print(greeting)
        
"""
We can mix positional and keyword arguments when calling a function,
but positonal arguments must come before keyword arguments. 
"""

result = add(2, b= 3) # Mixing positional and keyword arguments


            #  Function Attributes
"""
    setattr(object, name, value) 
The function is used to set the value of an attribute of an object. 
It allows us to set or modify the value of an attribute without explicitly using the dot notation. 
setattr(object, attribute_name, value)
"""

"""
    getattr(object, name)
Return the value of the named attribute of object. name must be a string.
If the sting  is the name of one of the object's attributes, the result is the value of that attribute. 
For example: getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, 
otherwise AttributeError is raised. 
"""

"""
    hasattr(object, name)
The arguments are an object and a string. 
This implemented by calling getattr(object, name) and seeing whether it raises an AttributeError or not. 
"""

"""
    delattr(object, name)
This is relative of setattr(). The arguments are an object and string.
The function deletes the named attribute. For example: delattr(x, 'foobar') is equivalent to del x.foobar
"""



         # Nested Scopes
def parent_function():
    def nested_function():
        print("Nested Function")
    print("Parent function")
    parent_function.nested_function = nested_function

parent_function()
parent_function.nested_function()



    # Getter and Setter Methods
def point(x, y):
    def set_x(new_x):
        nonlocal x
        x = new_x
    def set_y(new_y):
        nonlocal y
        y = new_y
    def get():
        return x, y
    point.set_x = set_x
    point.set_y = set_y
    point.get = get
    return point

print(point(5,5))

