import numpy as np 

"""
    Shape of an Array:
The shape of an array is the number of elements in each dimension. 

    Get the Shape of an Array
NumPy arrays have an attribute called 'shape' that returns a tuple with each index having
 the number of corresponding elements. 
"""
# Print the shape of a 2-D array:
arr = np.array([[1,2,3,4], [5,6,7,8]])
print(arr.shape)
"""
The example above returns (2,4) which means that the array has 2 dimensions, 
where the first dimension has 2 elements and the second has 4. 
"""

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr = np.array([1,2,3,4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


# We can change the shape of the array with the reshape, but it should be fit size. 
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newarr = arr.reshape(4,3)
print(newarr.shape)


# Use a correct NumPy method to change the shape of an array from 2-D to 1-D
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
newarr = arr.reshape(-1)
print(newarr.shape)