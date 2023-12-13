import numpy as np

"""
    Filtering Arrays:
    Getting some elements out of an existing array and creating a new array out of them is called filtering.
    In NumPy, you filter an array using a boolean index list.
"""

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)
"""
    The example above will return [41,43], why?
    Because the new array contains only the values where the filter array had the value True, in this case, index 0 and 2. 
"""  


arr = np.array([41,42,43,44])

filter_arr = []

for element in arr: 
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# Creating Filter Directly From Array
arr = np.array([41,42,43,44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# Creating a filter array that will return only even elements from the original array:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr) 