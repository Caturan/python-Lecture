import numpy as np 

"""
    Reshaping Arrays
Reshaping means changing the shape of an array. 
The shape of an array is the number of elements in each dimension. 
By reshaping we can add or remove dimensions or change number of elements in each dimensions. 
"""

# Convert the following 1-D array with 12 elements into a 2-D array. 
# The outermost dimension will have 4 arrays, each wtih 3 elements:
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)

# Convert the following 1-D array with 12 elements into a 3-D array. 
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements. 
newarr = arr.reshape(2,3,2) 
print(newarr)


"""
    Can we reshape into any shape? 
Yes, as long as the elements required for reshaping are equal in both shapes. 
We can rehsape an 8 elements 1D array into 4 elements in 2 rows 2D array
but we cannot reshape it into a 3 elements 3 row 2D array as that would require 3*3 = 9 elements.  
"""


# Returns Copy or View
arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4).base)
# The example above returns the original array, so it is a view. 


"""
    Unknown Dimension
We are allowed to have one "unknown" dimension. 
Meaning that we do not have to specify an exact number for one of the dimensions in the reshape method. 
Pass -1 as the value, and NumPy will calculate this number for you. 
"""
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,-1)
print(newarr)
# We cannot pass -1 to more than one dimension. 


"""
    Flatting the Arrays
Flatting array means converting a multidimensional array into a 1-D array. 
We can use reshape(-1) to do this. 
"""
arr = np.array([[1,2,3], [4,5,6]])
newarr = arr.reshape(-1)
print(newarr)
"""
Note: There are a lot of functions for changing the shapes of arrays in numpy flatten,
 ravel and also for rearranging the elements rot90, flip, fliplri flipud etc.
"""

