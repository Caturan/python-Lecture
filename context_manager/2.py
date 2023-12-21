
"""
    - Open and close
    - Lock and release
    - Change and reset
    - Create and delete
    - Enter and exit
    - Start and stop
    - Setup and teardown

    We can provide code to safely manage any of these pairs of operations in a context manager. 
    The we can reuse that context manager in with statements throughout our code. 
"""


"""
Coding Class-Based Context Managers:
    To implement the context manager protocal and create class-based context managers,
     we ned to add both the .__enter__() and the .__exit__() special methods to our classes. 

    .__enter__(self) -> This method handles the setup logic and is called when entering a new with context. Its return value is bound to the with target value.

    .__exit__(self, exc_type, exc_value, ext_tb) -> This method handles the teardown logic and is called when the flow of execution leaves the with context. 
     If an exception occurs, then exc_type, exc_value, and exc_tb hold the exception type, value, and traceback information respectively. 
"""

"""
    When the with statement executes, it calls .__enter__() on the context manager object to signal that we are entering into a new runtime context. 
     If we provide a target variable with the as specifier, then the return value of .__enter__() is assigned to that variable. 

    When the flow execution leaves the context, .__exit__() is called. If no exception occurs in the with code block, 
     then the three last arguments to .__exit__() are set to None. 
"""

# Sample
class HelloContextManager:
    def __enter__(self):
        print("Entering the context..")
        return "Hello"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context..")
        print(exc_type, exc_value, exc_tb, sep="\n")
    

with HelloContextManager() as hello:
    print(hello)

print()

with HelloContextManager():
    print()

print()

# exc_handling:
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True

with HelloContextManager() as hello:
    print(hello)
    hello[100]

print("Continue normally from here...")


