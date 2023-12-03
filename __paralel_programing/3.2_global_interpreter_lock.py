    # Global Interpreter Lock
"""
    GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode at once. 
    This lock can be significant limitation for CPU-bound problems but it is necessary mainly because CPython's memory management is not thread-safe. 

    To release GIL, we can switch to another Python implementation, such as Jython, IronPython, etc. 
    On the other, one can use numba module, which provides a just-in-time complier. Numba translates Python functions to optimized machine code at runtime using the industry-standard LLVM compiler library,
    which means in the firt run our functions is compiled and in the second run we get the best performance with the compiled version of our function. 

    The key point is to create functions correctly. Our function should be the atomic part of the solution and not use any complicated Python object. 
    For example, in our "Monte-Carlo Pi Estimator" problem, the function to be compiled with jit can be something like this: 
"""
def generate_points(n):
    inner = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            inner += 1
    return inner

''' If this function is a method of a class, then it should be a static method. Then we can relate our function with jit by using a decorator. '''  
@jit(nopython=True, nogil=True)
def generate_points(n):
    inner = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:
            inner += 1
    return inner