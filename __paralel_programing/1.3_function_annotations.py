    # Function Annotations
"""
    Python functions are defined by using def keyword, the name od the function and the parenthesized list of formal parameters.
    This line is called as the signature of the function. 
"""
def function_name():
    pass

# Arguments / Paramters
"""
    Python functions can have input arguments (we can also call them as parameters). Output arguments can be directly returned by using return keyword. 
"""

def fn(arg1, arg2):
    return arg1 + arg2

"""
    Arguments have three importnat property:
        - Default Value
        - Type Hint
        - Kind
"""

"""
Default Values:
    One can define the default values for arguments, which are used when the user doesn't provide any value for an argument. 
"""
def fn(arg1 = 0, arg2 = 0):
    return arg1 + arg2

"""
Type Hints:
    In Python, the type of the input and output arguments can be given as hints. 
    Keep in mind that Python does not have strict rules about the types, therefore when these hints are not followed, there will be no error raised. 
    If we want to check the types strictly, then we should that manually. The main purpose of the type hints is documentation. 
"""
def fn(arg1: int = 0, arg2: int = 0) -> int:
    return arg1 + arg2


"""
Kinds:
    The kind of an argument describes how the values are bound to the argument. The available kinds are:
        - Positional-or-Keywords(default kind)
        - Keyword-only
        - Positional -only
"""
# positional-or-keyword
def fn(arg1 = 0, arg2 = 0):
    return arg1 + arg2

fn()  # function can be called without argument values, because they have their default values
fn(3)  # you can provide values for some arguments
fn(3, 5)  # or you can provide values for all arguments
#fn(3, 5, 2)  # ERROR - but with this definition, you can't provide more than the number of predefined arguments
fn(arg1=3)  # you can also use these arguments as keyword
fn(arg1=3, arg2=5)  # both positional and keyword usage are allowed


# positional-or-keyword and keyword-only
# the arguments coming after '*' can only be keyword-only
def fn(arg1 = 0, arg2 = 0, *, arg3 = 1):
    return (arg1 + arg2) * arg3

fn(3, 5, arg3=2)  # to provide a value for arg3, you should use its name


# positional-only and positional-or-keyword and keyword-only
# the arguments before '/' are positional-only
# the arguments between '/' and '*' are positional-or-keyword
# the arguments after '*' are keyword-only
def fn(arg1 = 0, arg2 = 0, /, arg3 = 1, arg4 = 1, *, arg5 = 1, arg6 = 1):
    return (arg1 + arg2) * arg3 / arg4 * arg5**arg6

fn(3, 5, 2, arg4=4, arg5=7, arg6=8)  # combination of all kinds


"""
Parsing the Arguments with *args and **kwargs
    We don't have to define all arguments in the function's signature. We can parse the positona and keyword arguments as given below:
"""
def fn(*args, **kwargs):
    print(args)  # a tuple including the positional arguments
    print(kwargs)  # a dictionary including keyword arguments
"""
    Keep in mind that in a function call we should always provide the values of positional arguments first,
    after that we can provide the values of keyword arguments. 
"""

"""
Docstring:
    Docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. 
    Such a doctring becomes the __doc__ magic attribute of that object. 
"""
def fn(arg1 = 0, arg2 = 0):
    """This function sums two number."""
    return arg1 + arg2
"""
    With multi-line docstrings, we create the documentation of that object. 
    There some formats(reST, Google, Epytext,etc.) that some tools like Docutils and Sphinx use to automatically create documentations. 
"""

def fn(arg1 = 0, arg2 = 0):
    """
    This function sums two number.

    Args:
        arg1 (int): First number
        arg2 (int): Second number

    Returns:
        int: Sum of two numbers
    """
    return arg1 + arg2


