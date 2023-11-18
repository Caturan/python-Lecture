import numpy as np
# NumPy self work 
"""
NumPy is used for working with arrays. 

Why use NumPy? 
- NumPy aims to provide an array object that is up to 50x faster than traditional Python lists. 
- The array object in NumPy is called ndarray. 
"""

"""
Why is NumPy Faster Than Lists?
- NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
- This behavior is called locality of reference in computer science.
- This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.
"""

# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written C or C++. 

# Checking NumPy Version
print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(arr)

