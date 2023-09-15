"""

1. Missing Colons: Python uses colons to indicate the start of code blocks,
such as in 'if' statements, loops, and functions. Forgetting to include a colon will result in a syntax error. 

"""
# Incorrect 
"""

    if x > 5     (Missing Colon)
        print("x is greater than 5")

"""
# To fix it, add a colon at the end of the 'if' statement:
# Correct
x = 6
if x > 5: 
    print("x is greater than 5")



"""      

2. Indentation Errors: Python relies on consistent indentation to define code blocks. 
Mixing tabs and space or having inconsistent can lead to synxtax errors. 

"""
# Incorrect (mixxing tabs and spaces)
"""
def my_function():
("Hello, world!")
"""
# Correct (use spaces or tabs, but be consistent)
def my_function():
    print("Hello, World!")




"""

3. Invalid Variable Names: Variable names in Python must start with a letter or an underscore,
and can only contain letters, numbers, and underscores. Using invalid characters in variable names will result in a syntax error. 

"""
# Incorrect 
#   123abc = 42 

# Correct 
abc123 = 42
print(abc123)




"""

4. Incorrect Indentation Level: Make sure that all lines within a code block have the same level of indentation. 
Mismatched indentation will trigger an error. 

"""
"""

# Incorrect (inconsistent indentation)
if x > 5: 
    print("x is greater than 5")
   print("This line is indented incorrectly")

"""

# Correct (consistent indentation)
if x > 5:
    print("x is greater than 5")
    print("This line is indented correctly.")




"""

5. Incorrect Operator Usage: Using an operator in the wrong context can result in a syntax error. 
For example, using the '+' operator to concatenate strings requires both operands to be strings. 

"""

# Incorrect
#   result = "Hello" + 42  (Attempting to concatenate a string and an integer)

# Correct
result2 = "Hello" + str(42)   # (Convert the integer to a string before concatenation)
print(result2)


