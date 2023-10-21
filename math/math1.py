import math

""" 
    Python Math
Python has a set of built-in math functions, including an extensive math module,
that allows we us to perform mathematical tasks on numbers. 
"""

x = min(4, 15, 53)
y = max(53, 56, 7)

print(x)
print(y)


# The abc() function returns the absolute (positive) value of the specified number:
x = abs(-98)
print(x)


# The pow(x, y) function returns the value of the x to power of y. 
x = pow(4,2)
print(x)


"""
    The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions. 
To use it, we must import the math module. 
"""

x = math.sqrt(81)
print(x)


x = math.ceil(1.4)  # round upward nearest 
y = math.floor(1.4) # round downwords nearest 

print(x) 
print(y)


x = math.pi
print(x)
