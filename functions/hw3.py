# Some questions about the Python 

"""
Does a Python function always return a value?

In Python, a function does not always have to return a value. A function can return a value string the 'return' statement,
but it is not required to do so. If a function doesn't include a 'return' statement or includes a 'return' statement without an expression,
it implicitly return 'None'. 
"""

"""
How start to define a function in Python? 

def func():
"""


"""
What does return from call mltpl(2,3)?
The answer is below
"""
def mltpl(a, b=1):
    return a*b

print(mltpl(2,3))

"""
How can we use the following function to print exatly 'ParallelProgramming'?
"""
def a(x):
    def b(y):
        print(y, end='')
    print(x, end='')

a('Parallel'); a('Programming')

print()

"""
How can you change 'BC' with your own initials in the following function ?
"""
def speak(s):
    if not speak.who:
        speak.who = 'BC'
    print(f"{speak.who} says {s}")

"""
We can add an 'initals' parameter with a default value of 'BC'
We can pass our initals as an argument when calling the function,
which will override the default value and display our initials instead of 'BC'
""" 
def speak(s, initials='BC'):
    print(f"{initials} says {s}")

speak("Hello", initials='CAT')


import logging
"""
logging.info('Just a normal message')
logging.warning('Not fatal but still noted')
logging.error('There is something wrong')

def my_ugly_debug(s, level=0):
    pre_text = [
        "INFO",
        "WARNING",
        "ERROR" 
        ]

    print(f"{pre_text[level]: {s}}")
"""
# We decorated that func

# Configure the logging module
logging.basicConfig(level=logging.DEBUG) # Set the desired logging level

# Create a logger
logger = logging.getLogger("my_logger")

# Define a decorator for logging
def log_with_logging(func):
    def wrapper(s, level=0):
        pre_text = ["INFO", "WARNING", "ERROR"]
        message = f"{pre_text[level]}: {s}"
        logger.log(level, message)
        return func(s, level)
    return wrapper

# Define the existing function without changes
def my_ugly_debug(s, level=0):
    pre_text = [
        "INFO",
        "WARNING",
        "ERROR" 
        ]

    print(f"{pre_text[level]}: {s}")

# Decorate the function with the logging decorator
my_ugly_debug = log_with_logging(my_ugly_debug)

# Now, when we call my_ugly_debug, it will log message using the logging module
my_ugly_debug("This is an info message", level=0)
my_ugly_debug("This is a warning message", level=1)
my_ugly_debug("This is an error message", level=2)