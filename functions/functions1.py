# Python Functions
"""
A function is a block of code which only runs when its called. 
We can pass data, known as parameters, into a function.
A function can return data as a result.
"""

# In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")

# To call a function, use the function name followed by paranthesis:
my_function()


# Arguments
"""
Information can be passed into functions as arguments. 
Arguments are specified after the function name, inside the parantheses. 
We can add as many arguments as we want, just separate them with a comma. 

The following example has a function with one argument (fname). When the function is called:
 we pass along a first name, which is used inside the function to print the full name:
"""

def my_function(fname):
    print(fname, "TURAN")

my_function("Xezal")
my_function("Cevdet Ahmet")


# Arguments are often shortened to args in Python documentations. 

# The terms parameter and argument can be used for the same thing: information that are passed into a function. 
"""
From a function's perspective:
A parameter is the variable listed inside the parantheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

# By default, a function must be called with the correct number of arguments. 
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# Arbitrary Arguments, *args
"""
If you do not know how many arguments that will be passed into your function,
 add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Masal", "Arda", "Jack")


# Keyword Arguments
"""
We can also send arguments with the key = value syntax. 
This way the order of the arguments does not matter. 
"""
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# Arbitrary Keyword Arguments, **kwargs
"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
 ** before the parameter name in the function definition.
"""

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 


# Default Parameter Values
"""
The following example shows how to use a default parameter value. 
If we call the function without argument, it uses the default value:
"""
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("Brazil")


"""
We can send any data types of argument to a function(string, number, list, dictionary etc.)
And it will be treated as the same data type inside the function.
"""
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)



# Return Values
# To let a function return a value, use the return statement:
def my_function(x):
    return 5 * x 

print(my_function(3))
print(my_function(5))


# The pass Statement 
"""
function definitions cannot be empty, but if you for some reason have a function definition with no content,
 put in the pass statement to avoid getting an error.
"""
def my_function():
    pass



# Recursion
"""
Python also accepts function recursion, which means a defined function can call itself. 
Recursion is a common mathematical and programming comcept. It means that a function call itself. 
This has the benefit of meaning that we can loop through data to reach a result. 
"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(7)