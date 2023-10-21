
"""
What is a Module?
Consider a module to be the same as a code library. 
A file containing a set of function we want to include in our application. 
"""

"""
Create a Module
To create a module just save the code we want in a file with the file extension .py : 
"""

"""
Use a Module 
Now we can use the module we just created, by using the import statement.  
"""

def greeting(name):
    print("Hello " + name)


"""
Variables in Module
The module can contain functions, as already decribed, but also variables of all types(arrays, dictionaries, objects etc):
"""
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} 


"""
Naming a Module
We can name the module file whatever we like, but it must have the file extension .py
"""

"""
Re-naming a Module
We can create an alias when we import a module, by using the as keyword. 
"""

