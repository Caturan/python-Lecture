
# return and yield 

"""
    return
1-) Regular Functions:
Regular functions in Python are defined using the 'def' keyword and can perform a series of tasks or computations. 

2-) Returning a Specified Value:
The 'return' statement is used in regular functions to specify a value that the function should return the caller. 
It is typically used to provide the result of some computation. 

3-) Terminating the Function's Execution:
When a 'return' statement is encountered in a regular function, it immediately exits the function's execution. 
In other words, the function stops executing at that point. 

4-) State Lost after Return
Once a regular function returns a value string 'return', its state is lost. 
This means any variables, data, or context within function are cleaned up, 
and subsequent calls to the function will start the execution from the beginnin of the function. 

5-) Used to Compute a Value and Return It Immediately:
Regular functions that use 'return' are often used to compute a specific value and return it to the caller immediately. 
"""

def add(x, y):
    result = x + y
    return result

total = add(4, 4)
print(total)


"""
    yield
- 'yield' is used in the context of generators and is used to create an iterable sequences of values. 
- When a function containin yield is called, it does not execute the function's body immediately. Instead, it returns a genereator object. 
- The function's execution is paused when it encounters a yield statement, and the yielded value is returned to the caller. 
- Sunsequent calls to the generator's next() method resume the function's execution immediately after the last yield statement. 
- Generators allow or lazy evaluation, which means values are generated on-the-fly and not stored in memory, making them useful for iterating over large sequences. 
- When there no more values to yield, the generator raise 'StopIteration' exception. 
"""

def countdown(n):
    while n > 0:
        yield n
        n -= 1

counter = countdown(5)
for value in counter:
    print(value)


"""
In summary return is used to exit a regular function and return a value, 
while yield is used in generator functions to create iterable sequences and allows for lazy evaluation(call-by-need) of values. 
"""

def returning_squares(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result

def yielding_squares(n):
    for i in range(n):
        yield i**2

class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        result = self.i**2
        self.i += 1
        return result

def student_status():
    yield "Freshman"
    yield "Sophomore"
    yield "Junior"
    yield "Senior"
    


if __name__ == "__main__":
    print(type(returning_squares(5)))
    print(type(yielding_squares(5)))
    print(type(Squares(5)))

    print(dir(returning_squares(5)))
    print(dir(yielding_squares(5)))

    print(returning_squares(5))
    print(yielding_squares(5))
    print(Squares(5))

    i = yielding_squares(5)
    print(next(i), next(i), next(i), next(i), next(i))
    try:
        print(next(i))
    except StopIteration:
        print("End of iteration")

    for i in returning_squares(5):
        print(i, end=' ')
    print("End of returnin squares")

    for i in yielding_squares(5):
        print(i, end=' ')
    print("End of yielding squeares")

    for i in Squares(5):
        print(i, end=' ')
    print("End of squares")

    squares = Squares(5)
    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))
    try:
        print(next(squares))
    except StopIteration:
        print("End of iteration")
    
    for status in student_status():
        print(status, end=' ')
