"""
The try block lets us test a block of code for errors. 
The except block lets us handle the error. 
The else block lets us execute code when there is no error. 
The finally block lets us execute code, regardless of the result of the try-and except blocks. 
"""

"""
    Exception Handling
When an error occurs, or exception as we call it, Python will normaly stop and generate an error message. 
These exceptions can be handled using the try statement:
"""
try: 
    print(x)
except:
    print("An exception occured")
# Since the try block raises an error, the except block will be executed. 


"""
    Many Exceptions 
We can define as many exception blocks as we want: 
"""
# Print one message if the try block raises a NameError and another for other errors:
try: 
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


"""
    Else
We can use the else keyword to define a block of code to be executed if no errors were raised:
"""
try: 
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


"""
    Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not. 
"""
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")



"""
    Raise an exception
As a Python developer we can choose to throw an exception if a condition occurs. 
To throw (or raise) an exception, use the raise keyword. 
"""

# Raise an error and stop the program if x is lower than 0:
x = -1 

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# The raise keyword is used to raise an exception. We can define what kind of error to raise, and the text to print to the user. 
x = "Hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
