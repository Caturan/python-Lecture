# Acces Items
"""
We cannot acces items in a set by referring to an index or key. 
But we can loop through the set items using a for loop, 
or ask if a specified values is present in a set, by using the in keyword. 
"""

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


# Check if "banana" is present in the set:
print("banana" in thisset)



# Add items 
# Once a set is created, we cannot change its items, but we can add new items. 
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


# To add items from another set into the current set, use the update() method. 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineaplle", "mango", "papaya"}

thisset.update(tropical)
print(thisset)


# Add Any Iterable 
"""
The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc. )
""" 

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)



# Remove Item
# To remove an item in a set, use the remove(), or the discard() method. 
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error. 

thisset.discard("apple")
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error. 

"""
 We can also use the pop() method to remove an item, but this method will remove a random item, 
 so we cannot be sure what items that gets removed. 
"""

thisset = {"apple", "cherry", "banana"}

x = thisset.pop()

print(x)
print(thisset)


# The clear() method empties the set:
thisset.clear()
print(thisset)


# The del keyword will delete the set completely:
thisset = {"banana", "apple", "cherry"}

del thisset
print(thisset)