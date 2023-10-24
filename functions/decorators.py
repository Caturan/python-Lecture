"""
Python decorators are a powerful and advanced feature that allows you to modify or enhance the behavior of functions or methods without changing their code.
Decorators are often used for tasks such as logging, authentication, memoization, and more.
"""

def my_decorator(func):
    def wrapper():
        print("Before func is called")
        func()
        print("After func is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


def d1(fn):
    def _d1():
        print("Before d1")
        fn()
        print("After d1")
    return _d1

@d1
def f1():
    print("function")

f1()


    # Decorator Chain
def decorator1(fn):
    def wrapper(*args, **kwargs):
        print("Decorator1: Before function call")
        result = fn(*args, **kwargs)
        print("Decorator1: After function call")
        return result
    return wrapper

def decorator2(fn):
    def wrapper(*args, **kwargs):
        print("Decorator2: Before function call")
        result = fn(*args, **kwargs)
        print("Decorator2: After function called")
        return result
    return wrapper

@decorator1
@decorator2
def my_function():
    print("My function is called")

my_function()