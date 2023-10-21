import module1 as mod1
import platform

# Import the module named module1, and call the greeting function: 
mod1.greeting("Ahmet")

a = mod1.person1["age"]
print(a)


"""
Built-in Modules 
There are several built-in modules in Python, which we can import whenever we like. 
For example platform module:
"""
x = platform.system()
print(x)

"""
Using the dir() Function
There is a built-in function to list all the function names (or variables names) in a module.
The dir() function:
""" 
# List all the defined names belonging to the platform module:
x = dir(platform)
print(x)

# Note : The dir() function can be used on all modules, also the ones we create ourself. 

