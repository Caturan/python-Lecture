x = memoryview(b'clcoding')
print(type(x))

"""
    In Python, memoryview is a build-in class that allows you to access the memory of an object without copying it.
    This can be useful for performance reasons, especially when dealing with large data sets or when you want to manipulate data in place.
"""

"""
    b'clcoding' is a bytes object. 
"""

"""
    Why use memoryview?
        Efficiency: It allows us to access and manipulate data without copying it, 
        which can save memory and improve performance.

        Slicing and indexing: We can use memoryview to slice and index data structures such as bytes,
        bytearray, and other objects that support the buffer protocal. 
"""

# Example Usage

data = b'clcoding'
mv = memoryview(data)

# Accessing elements:
print(mv[0]) # return the ascii value of 'c'

# Slicing:
print(mv[1:4]) # a slice of memoryview

# Converting back to bytes
print(mv.tobytes())