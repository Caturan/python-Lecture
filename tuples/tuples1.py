# Tuples

mytuple = ("apple", "banana", "cherry")

"""
Tuples are used to store multiple items in a single variable. 
A tuple is a collection which is ordered and unchangeable. 
Tuples are written with round brackets. 
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# Tuple Items
"""
Tuple items are ordered, unchangeables, and allow duplicate values. 
Tuple items are indexed, the first item has index [0]. 
"""

# Ordered
"""
When we say that tuples are ordered, it means that the items have a defined order,
and that order will not change. 
"""

# Unchangeable
"""
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
"""

# Allop Duplicates 
# Since tuples are indexed, they can have items with the same value. 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


# Length 
# Use the len() function:
print(len(thistuple))


# Create Tuple With One Item
"""
To create a tuple with onyl one item, we have to add a comma after the item,
otherwise Python will not recognize it as a tuple.
"""
thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))


# Tuple items can be any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False) 

# A tuple can contain different data types:
tuple1 = ("abc", 45, True, 64, "girl")


# type()
"""
From Python's perspective, tuples are defined as objects with the data type 'tuple':
<class 'tuple'>
"""

# The tuple() Construcotr
# It is also possible to use the tuple() constructor to make a tuple
thistuple = tuple(("apple","banana", "cherry"))
# note the double round-brackets
print(thistuple)
