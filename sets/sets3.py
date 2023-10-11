# Join Sets 
"""
There are several ways to join two or more sets in Python.
We can use the union() method that returns a new set containing all items from both sets, 
or the update() method that inserts all the items from one set into another:
""" 

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# The intersection_update() method will keep only the items that are present in both sets. 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)


# The intersection() method will return a new set, that only contains the items that are present in both sets. 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)


# The symmetric_difference_update() method will keep onyl the elements that are NOT present in both sets. 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x) 

# The symmetric_difference() method will return a new set, that contains onyl the elements that are NOT present in both sets. 

"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""