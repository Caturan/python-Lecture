# Python Sets

myset = {"apple", "banana", "cherry"}

"""
Sets are used to store multiple items in a single variable.
A set is collection which is unordered, unchangeable*, and undindexed. 
Sets are written curly brackets. 
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)


# Sets items do not allow duplicate values. 

# Unordered
"""
Unordered means that the items in a set do not have a defined order. 
Set items can appear in a different order every time we use them, 
and cannot be referred to by index or key. 
"""


# Once a set is created, we cannot change its items, but we can remove items and add new items. 

# Sets cannot have two items with the same value. 
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset) 


# The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = { "apple", "banana", "cherry", True , 1, 2}
print(thisset)


# We get number of items with len() func:
print(len(thisset))


# type()
# From Python's perspective, sets are defined as objects with the data type 'set':
# < class 'set'>
print(type(thisset))


# It is also possible to use the set() constructor to make a set. 
thisset = set(("apple", "banana", "cherry")) # note the double round-brakcets
print(thisset)

