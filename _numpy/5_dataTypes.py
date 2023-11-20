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
We use the array() function to create arrays, this function can take an optional argument:
dtype that allows us to define the expected data type of the array elements:
"""
arr = np.array([1,2,3,4], dtype='S')
print(arr)
print(arr.dtype)


# For i, u, f, S and U we can define size as well. 
arr = np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)


"""
    What if a Value can not be Converted?
If a type is given in which elements can't be casted the NumPy will raise a ValueError. 
ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect. 
"""
"""
arr = np.array(['a','2','3'], dtype='i')
print(arr)
"""
"""
    Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
The astype() function creates a copy of the array, and allows us to specify the data type as a parameter. 
The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or we can use the data type directly like float for float and int for integer. 
"""
# Change data type from float to integer by using 'i' as parameter value:
arr = np.array([1.1,2.2,3.2])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# Change data type from float to integer by using int as parameter value:
arr = np.array([1.2,2.3,3.1])
newarr = arr.astype(int) 
print(newarr)
print(newarr.dtype)

# Change data type from integer to boolean:
arr = np.array([1,0,3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
