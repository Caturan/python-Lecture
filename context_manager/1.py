"""
    The with statement in Python is a quite useful tool for properly managing external resources in our programs. 
    
    It allows us to take advantage of existing context managers to automatically handle the setup and teardown phases 
    whenever we are dealing with external resources or with operations that require those phases.  
"""

file = open("hello.txt", "w")
file.write("hallo")
file.close()

"""
    In Python, we can use two general approaches to deal with resource manangement. We can wrap our code in:
    1. A try...finally contruct
    2. A with construct
"""
# The try...finally Approach
file = open("hello.txt", "w")

try:
    file.write("Hello World")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()


# The with Statement Approach
"""
    The Python with stament created a runtime context that allows us to run a group of statements under the control of a context manager. 
"""

"""
    To write a with statement, we need to use the following general syntax: 
    
    with expression as target_var:
        do_something(target_var)

    This protocal consists of two speial methods:
    1. __enter__() is called by the with statement to enter the runtime context. 
    2. __exit__() is called when the execution leaves the with code block.

    The as specifier is optional. If we provide a target_var with as, the the return value of calling __enter__() on the context manager object is bound to that variable. 
   
    Note: Some context managers return None from __enter__() because they have no useful objects to give back the caller. 
    In these cases, specifying a target_var makes no sense. 

    Here' how the with statement proceeds when Python runs into it:
    1. Call expression to obtain a context manager. 
    2. Store the context manager's .__enter__() and .__exit__() methods for later use. 
    3. Call .__enter__() on the context manager and bind its return value to target_var if provided. 
    4. Execute the with code block. 
    5. Call .__exit__() on the context manager when the with code block finishes. 

    That's why the with statement is so useful. It makes properly acquiring and releasing resources a breeze. 
"""

"""
    Here' how to open our hello.txt file for writing using the with statement:
    
    with open("hello.txt", mode="w") as file:
        file.write("HelloWorld)

    This object is also a context manager, so the with statement calls .__enter__() and assigns its return value to file. 
    Then we can manipulate the file inside the with code block. When the code block ends, .__exit__() automatically gets called and closes the file for us, 
    even if an exception is raised inside the with block. 

    This with construct is shorter than its try … finally alternative, but it's also less general, as we already saw. 
    We can only use the with statement with objects that support the context management protocol,
    whereas try … finally allows us to perform cleanup actions for arbitrary objects without the need for supporting the context management protocol.
"""

"""
Summarizing the with Statement's Advantages:
    - Makes resource management safer than its equivalent try...finally statemens
    - Encapsulates standard uses of try...finaly statements in context managers. 
    - Allows reusing the code that automatically manages the setup and teardown phases of a given operation. 
    - Helps avoid resource leaks 
"""

