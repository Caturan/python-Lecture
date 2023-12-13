import numpy as np 

"""
    Searching Arrays:
    We can search an array for a certain value, and return the indexes that get a match. 
    To search an array, use the where() method. 
"""

arr = np.array([1,2,3,4,5,4,4])
x = np.where(arr == 4)
print(x)


arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2 == 0)
print(x)

"""
    Search Sorted
    There is a method called searchsorted() which performs a binary search in the array,
     and returns the index where the specified value would be inserted to maintain the search order.
"""
# The searchsorted() method is assumed to be used on sorted arrays. 
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x) 


"""
    By default the left most index is returned, but we can give side='right' to return the right most index instead. 
"""
x = np.searchsorted(arr, 7, side='right')
print(x)
