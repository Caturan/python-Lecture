from module1 import person1

"""
Import From Module
We can choose to import only parts from a module, by using the from keyword. 
"""

"""
The module named module1 has one function and one dictionary. 
Import only the person1 dictionary from the module: 
"""
print(person1["country"])

#When importing using the from keyword, do not use the module name when referring to elements in the module.  