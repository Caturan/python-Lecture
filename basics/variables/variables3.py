# Local and Global Variables

"""

In Python, you can have both local and global variables in the same program. These variables serve different purposes and have different scopes:

Local Variables:
* Local variables are defined within the scope of a function or a code block, such as a loop or conditional statement.
* They are only accessible within the function or block where they are defined.
* Local variables are created when the function or block is entered and destroyed when it exits, making them temporary in nature.
* They shadow (take precedence over) global variables with the same name within their scope.

"""

def my_function():
    local_var = 10  # This is a local variable
    print("Inside the function:", local_var)

my_function()
# Attempting to access local_var here would result in an error


"""
Global Variables:
* Global variables are defined outside of any function or code block, at the top level of the script or module.
* They are accessible from any part of the program, including functions and code blocks.
* Global variables have a more extended lifetime and persist throughout the program's execution.
* They can be accessed and modified from both the global scope and within functions using the global keyword.
"""

global_var = 20  # This is a global variable

def my_function():
    global global_var  # Using the global keyword to access the global variable
    global_var += 5    # Modifying the global variable
    print("Inside the function:", global_var)

my_function()
print("Outside the function:", global_var)


