    # Decorators
"""
    Decorators take a function as argument and returns a function. 
    They are used to extend the behaviour of the wrapped function, without modifying it. 
    So they are very useful for dealing with code legacy. 
"""

"""
Decorators as a Design Pattern
    We can define decorators in any programming language by using the following design pattern:
"""
def my_decorator(fn):
    def _my_decorator():
        print("Before the function")
        fn()
        print("After the function")
    return _my_decorator

def my_decorated_function():
    print("Function")

# with this usage you should create a new object once by using decorator manually
my_decorated_function = my_decorator(my_decorated_function)
''' Note that we are using a single leading underscore to follow the "inner use" convention. '''

"""
Decorators in Python:
    In Python we can relate our function wtih decorators by using a line starting with @ before the function's signature. 
"""
def my_decorator(fn):
    def _my_decorator():
        print("Before the function")
        fn()
        print("After the function")
    return _my_decorator

@my_decorator
def my_decorated_function():
    print("Function")

my_decorated_function()
print()
"""
Decorators with Arguments
    Most of the time we should also pass the arguments to the wrapped functions. 
    We can use *args and **kwargs to do this easily. We can also modify the input arguments or return values as we wish. 
"""
def decorator(func):
    def _decorator(*args, **kwargs):
        print("Before the function")
        print(args)
        print(kwargs)
        func(*args, **kwargs)
        print("After the function")
    return _decorator

@decorator
def decorated_func_w_args(x):
    print(f"x = {x}")

decorated_func_w_args(5)
print()

"""
    We may also want to use seperate arguments for a decorator. 
    We can create a decorator which can accept its own parameters by adding one more level as follows:
"""
def decorator(arg1, arg2):
    def real_decorator(func):
        def _decorator(*args, **kwargs):
            print(f"The arguments are: {arg1}, {arg2}")
            print("Before the function")
            print(args)
            print(kwargs)
            func(*args, **kwargs)
            print("After the function")
        return _decorator
    return real_decorator

@decorator("Cevdet", "Ahmet")
def my_function(s):
    print(s)

my_function("Parallel Programming")

print()
"""
    If we need to use a more complex setup, we can also define our decorator as a class by using its __call__ method:
"""
class DecoratorClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def decorator(*args, **kwargs):
            print(f"The arguments are: {self.arg1}, {self.arg2}")
            print("Before the function")
            print(args)
            print(kwargs)
            func(*args, **kwargs)
            print("After the function")
        return decorator

@DecoratorClass("Bora", "Canbula")
def my_function(s):
    print(s)

my_function("Parallel Programming")

print()

@decorator("Celal", "Bayar")
@DecoratorClass("Cevdet", "Ahmet")
def my_function(s):
    print(s)

my_function("Parallel Programming")


