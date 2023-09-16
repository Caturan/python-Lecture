
""" 
There are three numeric types in Python:
* int        
* float      
* complex   
"""

x = 1
y = 2.8
z = 1j

# To verify the type of any object in Python, use the type() function:
print(type(x))
print(type(y))
print(type(z))


"""
* Int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

* Float

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
Float can also be scientific numbers with an "e" to indicate the power of 10. 

* Complex Numbers (complex):

Complex numbers have both a real part and an imaginary part, denoted by j or J.
They are often used in mathematical and scientific computations.


"""
k = -89.7e21
print(type(k))

l = 32E12
print(type(l))



# Numeric operations
a = 5
b = 2

# Addition
result_add = a + b  
print(result_add)

# Subtraction
result_sub = a - b  
print(result_sub)

# Multiplication
result_mul = a * b  
print(result_mul)

# Division
result_div = a / b  
print(result_div)


"""
Python also provides some additional functions and modules for more advanced mathematical operations. 
For example, we can use the 'math' module for functions like square root, trigonometric functions, logarithmic etc
"""
import math
# Square root
sqrt_result = math.sqrt(25)
print(sqrt_result)

# Trigonometric functions 
sin_result = math.sin(math.radians(30))
print(sin_result)


"""
Type Conversion
We can convert from one type to another with the int(), float(), and complex() methods:
"""

q = 1    # int
w = 2.8  # float
e = 1j   # complex

#convert from int to float:
t = float(x)

#convert from float to int:
y = int(y)

#convert from int to complex:
u = complex(x)

print(t)
print(y)
print(u)

print(type(t))
print(type(y))
print(type(u)) 


# Type casting
num = 42.5
integer_num = int(num)        # Converts to integer: 42
float_num = float(integer_num)  # Converts to float: 42.0


"""
* Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers: 
"""

import random
print(random.randrange(1, 10))