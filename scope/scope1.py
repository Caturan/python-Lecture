# Python Scope

# A variable is only available from inside the region it is created. This is called scope. 

"""
Local Scope
A variable created inside a function belongs to the local scope of that function, 
and can only be used inside that function. 
"""

def myfunc():
    x = 300
    print(x)

myfunc()

"""
Function Inside Function
As explained in the example above, the variable x is not available outside the function,
but it is available for any function insdie the function:
"""
def myfunc():
    x = 200
    def myinnerfunc():
        print(x)
        myinnerfunc()

myfunc()


"""
Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the globel scope. 
Global variables are available from within any scope, global and local. 
"""
x = 100
def myfunc():
    print(x)

myfunc()

print(x)


"""
Naming Variables
If we operate with the same variable name inside and outside of a function, 
Python will treat them as two seperate variables, one available in the global scope (outside the function)
and one available in the local scope (inside the function)
"""
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)


"""
Global Keyword
If we need to create a global variable, but are stuck in the local scope, we can use the global keyword. 
The global keyword makes the variable global. 
"""
def myfunc():
    global x 
    x = 300

myfunc()

print(x)


# Also use the global keyword if we want to make a change to a global variable inside a function. 
x = 300

def myfunc():
    global x
    x = 200 

myfunc()

print(x)

