myList = ["apple", "banana", "cheery"]


"""
Lists are used to store multiple items in a single variable. 
Lists are one of 4 built-in data types in Python used to store collections of data, 
 the other 3 are Tuple, Set and dictionary, all with different qualities and usage. 
Lists are created using square brackets: 
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)


# List items
"""
List items are ordered, changeable, and allow duplicate values. 
List items are indexed, the first item has index [0], the second item has index [1] etc. 
"""

# Ordered 
"""
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If we add new items to a list, the new items will be placed at the end of the list.  
"""

# Changeable
"""
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created. 
"""

# List allow duplicate values: 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# To determine how many items a list has, use the len() function:
print(len(thislist))


# List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# A list can contain different data types:
list1 = ["abc", 32, True, 43, "male"]


# type()
"""
From Python's perspective, lists are defined as objects with the data type 'list':
<class 'list'>
"""
print(type(myList))


# The list() constructor
"""
It is also possible to use the list() constructor when creating a new list
"""
thislist = list(("apple," "banana", "cherry")) # note the double round-brackets
print(thislist)
print(type(thislist))