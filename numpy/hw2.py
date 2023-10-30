import numpy as np

#print(dir(np))

print(np.array([1, 4, 56]))

# What is the correct way to print 5 from the array given below?
a = np.array([[1, 2], [3, 4], [5, 6]])
print(a)
print(a[2, 0])


# What is the correct way to print every other item from the array given below?
a = np.arange(5)
print(a)
print(a[0:5])


# What does the shape mean  of a NumPy array? -> Numbers of items in each dimension. 


# What is the output the code below? 
n_1 = np.array([1, 2, 3])
n_2 = np.array([4, 5, 6])
n_3 = np.array([7, 8, 9])
print(np.array([n_1, n_2, n_3]).ndim)

# What is the output of the code below? 
print(np.array([n_1 + n_2 + n_3]).shape)


# Which of the following is created with the code given below? 
n = np.array([[1, 2, 3], [4, 5, 6]])
print(n.ndim, n.shape)
# 2-d array of shape 2 * 3


# What is the output of the code below? 
print(np.arange(10).reshape(2, -1))
# First digit is the x-axis , with -1 is the program automatically seperate the data.  


# What is the output of the code below? 
print(np.array([0.5, 1.5, 2.5]).dtype) # -> float64