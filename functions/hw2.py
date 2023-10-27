"""
A decorator which measures the performance of functions and 
also saves some statistics.
Has three attributes: counter, total_time, total_mem
Attribute counter stores the number of times that the decorator 
has been called.
Attribute total_time stores the number of total time that the 
functions took.
Attribute total_mem stores the total memory in bytes that the
functions consumed.
"""
import tracemalloc
import time

#print(dir(tracemalloc))

def performance(fn): 
    def wrapped_function(*args, **kwargs):  
        tracemalloc.start()  # Start tracking memory usage
        start_time = time.perf_counter()  # Start measuring the time of the process
        result = fn(*args, **kwargs)  # Call the wrapped function with the given arguments and get the result
        end_time = time.perf_counter()  # Finish measuring the time of the process
        mem_used = tracemalloc.get_traced_memory()[1]  # Get the traced memory usage

        if not hasattr(performance, 'counter'):
            # If 'counter' attribute doesn't exist in the wrapped function, initialize it along with 'total_time' and 'total_mem'
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter += 1  # Increment the counter for each function call
        performance.total_time += end_time - start_time  # Update the total time with the current function's execution time
        performance.total_mem += mem_used  # Update the total memory usage with the current function's memory usage
        return result  # Return the result of the wrapped function

    return wrapped_function  # Return the wrapped function as the decorator

# Sample function decorated with 'performance'
@performance
def example_function(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

# Call the decorated function
result = example_function(1000000)

# Access the statistics
print("Function Calls:", performance.counter)
print("Total Time:", performance.total_time, "seconds")
print("Total Memory:", performance.total_mem, "bytes")
