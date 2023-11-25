"""
In Python, a function that contains the yield keyword is called generater function. 
The main difference between a regular function and a generator function lies in their execution and the way the generate values. 

1. Regular Functions: They use the return statement to return a value and the the function exists. 
 When called again, it starts execution from the beginning. 

2. Generator Function: They use the yield statement to produce a series of values one at a time. 
 When the yield statement is encountered, the function's state is frozen, but it retains its state, 
 allowing it to continue execution from where it left off when called again. 
 This means the function is paused rather than exited when yieldin a value. 
"""
def simple_generator():
    yield 1
    yield 2
    yield 3 

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen)) # Stop iteration because there are no more values 

"""
Generators are memory efficient because they generate values on-the-fly and do not store the entire sequence in memory,
 making them useful for handling large amounts of data or generating an infinite sequence of values. 
"""

