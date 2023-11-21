import numpy as np 
"""
    Iterating Arrays
Iterating means going through elements one by one. 
As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python. 
If we iterate on a 1-D array it will go through each element one by one. 
"""

arr = np.array([1,2,3])
for x in arr:
    print(x)


# In a 2-D array it will go through all the rows. 
arr = np.array([[1,2,3], [4,5,6]])
for x in arr:
    print(x)

# To return the actual values, the scalars, we have to iterate the arrays in each dimension. 
for x in arr:
    for y in x:
        print(y)

    

# Iterating 3-D arrays -> In a 3-D array it will go through all the 2-D arrays. 
arr = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])

for x in arr:
    print(x)

# To return the actual values, the scalars, we have to iterate the arrays in each dimension. 
for x in arr:
    for y in x:
        for z in y:
            print(z)


"""
    Iterating Arrays Using nditer()
The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
It solves some basic issues which we face in iteration. 
"""
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x) 


"""
    Iterating Array with Different Data Types
We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating. 
NumPy does not change the data type of the element in-place (where the elements is in array) so it needs some other space to perform this action, that extra space is called buffer, 
and in order to enable it in nditer() we pss flags=['buffered'].  
"""

arr = np.array([1,2,3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)


# We can use fitering and followed by iteration. 
# Itereate through every scalar element of the 2D array skipping 1 element:
arr = np.array([[1,2,3,4], [5,6,7,8]])
for x in np.nditer(arr[:,::2]):
    print(x)


"""
    Enumareted Iteration Using ndenumerate():
Enumeration means mentionaning sequence number of somethings one by one. 
Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases. 
"""
arr = np.array([1,2,3,4])

for idx, x in np.ndenumerate(arr):
    print(idx, x)

# Enumerate on following 2D array's elements:
arr = np.array([[1,2,3,4], [5,6,7,8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

