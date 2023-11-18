import numpy as np
"""
NumPy has some extra data types, and refer to data types with one character, 
like i for integers, u for unsigned integers etc.

i - integer
b - boolean 
u - unsigned integer
f - float 
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string 
V - fixed chunk of memory for other type (void)
"""

# The NumPy array object has a property called dtype that returns the data type of the array:
arr = np.array([1,2,3,4])
print(arr.dtype)

"""
We use the array() function to create arrays, 
"""
arr = np.array([1,2,3,4], dtype='S')
print(arr)
print(arr.dtype)

