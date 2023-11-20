import numpy as np

"""
    Access Array Elements
Array indexing is the same as accessing an array element. 
We can acces an arrray element by referring to its index number. 
The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.
"""

arr = np.array([1,2,3,4])
print(arr[0])


print(arr[2] + arr[3])


"""
    Access 2-D Arrays
To access elements from 2-D arrays we can use comma seperated integers representing the dimension and the index of the element. 
Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represenets the column. 
"""
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])


"""
    Access 3-D Arrays
To access elements form 3-D arrays we can use the comma seperated integers representing the dimensions and the index of the element. 
"""
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) 


# Negative indexing to access an array from the end. 
