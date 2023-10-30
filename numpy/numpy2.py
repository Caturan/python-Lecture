# Numpy Arrays

"""
Numerical Python (NumPy) is a powerful library for numerical computing. 
Its key feature is multi dimonsial arrays (ndarrays)
"""

# Traditional Python Lists
"""
• Dynamically Typed: Lists can store elements of mixed types in a 
single list.
• Resizable: Lists can be resized by appending or removing 
elements.
• General-purpose: Lists are general-purpose containers for items 
of any type.
• Memory: Lists have a larger memory overhead because of their 
general-purpose nature and dynamic typing.
• Performance: Basic operations on lists may not be as fast as 
those on NumPy arrays because they aren't optimized for 
numerical operations.
"""

# NumPy Arrays
"""
• Typed: All elements in a NumPy array are of the same type.
• Size: The size of a NumPy array is fixed upon creation. However, 
one can create a new array with a different size, but resizing inplace (like appending in lists) isn't directly supported.
• Efficiency: NumPy arrays are memory-efficient as they store 
elements in contiguous blocks of memory.
• Performance: Operations on NumPy arrays are typically faster 
than lists, especially for numerical tasks, due to optimized C and 
Fortran extensions.
• Vectorized Operations: Supports operations that apply to the 
entire array without the need for explicit loops (e.g., adding two 
arrays element-wise).
• Broadcasting: Advanced feature allowing operations on arrays of 
different shapes.
• Extensive Functionality: Beyond just array storage, NumPy 
provides a vast range of mathematical, logical, shape 
manipulation, and other operations.
• Interoperability: Can interface with C, C++, and Fortran code.
"""
