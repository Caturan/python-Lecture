# Python Lambda
"""
A lambda function is a small anonymous function. 
A lambda function can take any number of arguments, but can only have one expression. 
"""
# lambda arguments : expression

# Add 10 to argument a, and a + 10
x = lambda a : a + 10
print(x(5))

# Lamba functions can take any number of arguments:

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5,6))

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


"""
Why use Lambda Functions? 
The power of lambda is better shown when we use them as an anoynmous function inside another function. 

Say we have function definiton that takes one argument,
 and that argument will be multiplied with an unknown number:
"""
def my_function(n):
    return lambda a : a * n

# Use that function definiton to make a function that always doubles the number we send in:
mydoubler = my_function(2)
print(mydoubler(11))

mytripler = my_function(3)
print(mytripler(23))

# Use lambda functions when an anonymous function is requried for a short period of time. 
