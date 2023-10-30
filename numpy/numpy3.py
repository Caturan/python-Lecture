import numpy as np 
import timeit


print(dir(np))

def an_array():
    n = np.arange(10)
    print(n, type(n))


pyhon_list = [i for i in range(1000)]
numpy_array = np.arange(1000)

print(dir(timeit))

help(timeit.timeit)


# What is the ''' ''' in Python? 
long_text = '''
This is a multi-line string.
It preserves line breaks and formatting.
You can use triple-quotes with single or double quotes.
'''
print(long_text)

# standard Python
standard_statement = \
'''
s = 0
for i in range(10000):
    s += i
'''
# standard Python with list comprehension
standard_plus_statement = \
'''
n = [i for i in range(10000)]
s = sum(n)
'''
# Numpy array
numpy_statement = \
'''
import numpy as np
n = np.arange(10000)
s = np.sum(n)
'''

print(timeit.timeit(standard_statement, number=1000))

print(timeit.timeit(standard_plus_statement, number=1000))

print(timeit.timeit(numpy_statement, number=1000))

print()

"""
Numpy arrays are stored at one continuous place in memory, so processes can access and manipulate them very efficiently. 
This behaviour is called locality of referece in computer science. 
"""

# NumPy Arrays
"""
0 - Dimensional Array: Scalar
1- Dimensional Array: Vector
2 - Dimensional Array: Matrix
N-D Array
"""

a_scalar = np.array(17)
print(a_scalar, type(a_scalar))

a_vector = np.array([4, 5])
print(a_vector, type(a_vector))

a_vector_from_tuple = np.array((3, 5, 7))
print(a_vector_from_tuple, type(a_vector_from_tuple))

a_vector_from_set = np.array({3,5,3,5,6,3,5,6,7,2})
print(a_vector_from_set, type(a_vector_from_set))

# Array can take different variables 
an_array_with_chars = np.array(['a', "Cevdet", 35])
print(an_array_with_chars, type(an_array_with_chars))

two_d_array = np.array([[1, 2, -1], [5, 5, 9]])
print(two_d_array, type(two_d_array))

# indexing with multiple dimensions
print(two_d_array[:, 1:])
# higher dimensions
m_1 = np.array([[11, 12, 13],
                [14, 15, 16],
                [17, 18, 19]])
m_2 = np.array([[21, 22, 23],
                [24, 25, 26],
                [27, 28, 29]])
m_3 = np.array([[31, 32, 33],
                [34, 35, 36],
                [37, 38, 39]])
m = np.array([m_1, m_2, m_3])

print(m)
print(dir(m))

print(m.shape,m.ndim)
# The shape attribute returns a tuple that specifies the dimension of array. 
# The ndim attribute returns an integer that indicates how many dimensions(degree) array. 

# reshape change the dimensions of the array or define the dimensions 
n = np.arange(10)
print(n.reshape(2, -1))
# We use to -1 automatically numPy decide of the dimension. 


"""
View and Copy Concept in NumPy
* view affected by the changes made to the original array
* copy not affected by the changes made the original array
"""

# Data Types in Python vs Numpy
def _typecodes():
    print(np.typecodes)


def _sctypes():
    print(np.sctypes)


"""
Data Types in NumPy:
- i integer
- b boolean
- u unsigned integer
- f float
- c complex float
- m timedelta
- M datetime
- O object
- S string
- U unicode string
- V fixed chunk of memory for other type
"""


def main():
    print("Hello")
    an_array()

    _typecodes()
    _sctypes()


if __name__ == "__main__":
    main()

