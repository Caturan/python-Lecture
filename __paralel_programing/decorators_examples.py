
"""
    Q1: Write a Python program to create a decorator that logs the arguments and return value of a function. 
"""
def decorator(func):
    def wrap(*args, **kwargs):       
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrap

@decorator
def multiply_numbers(x, y):
    return x * y

result = multiply_numbers(10, 20)
print("Result:", result)


"""
    Write a Python program to create a decorator function to measure the execution time of a function. 
"""
import time

def time_decorator(fn):
    def my_decorator():
        start_time = time.time()
        fn()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(elapsed_time)
    return my_decorator

@time_decorator
def time_fn():
    print("Time")

time_fn()


def convert_to_data_type(data_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return data_type(result)
        return wrapper
    return decorator

@convert_to_data_type(int)
def add_numbers(x, y):
    return x + y

result = add_numbers(10, 20)
print("Result:", result, type(result))

@convert_to_data_type(str)
def concatenate_strings(x, y):
    return x + y

result = concatenate_strings("Python", " Decorator")
print("Result:", result, type(result))


