# Access items
# List items are indexed and we can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative indexing
""" 
Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc. 
"""
print(thislist[-2])

# Range of Indexes 
"""
We can specify a range of indexes by specifying where to start and where to the end the range. 
When specify a range, the return value will be a new list with the specified items. 
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# Check if item exists
# To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 



#  Change List Items 

# To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "orange"
print(thislist)


# Change a range of item values
""" 
To items the value of items within a specific range, define a list with the new values, 
and refer to the range of index numbers where we want to insert the new values:
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# Insert Items
"""
To insert a new list item, without replacing any of the exsiting values, we can use the insert() method. 
The insert() method inserts an item at the specified index:
"""
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
thislist.insert(4, "orange")
print(thislist)


# Append items
# To add an item to the end of the list, use the append() method:
thislist.append("orange")
print(thislist)


# Extend List
# To append elements from another list to the current list, use the extend() method. 
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add Any Iterable
# The extend() method does not have to append lists, we can add any iterable object(tuples, sets, dictionaries etc.)
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Specified Item
# The remove() method removes the specified item. 

thislist.remove("cherry")
print(thislist)


# The pop() method removes the specified index. 
# If we do not specify the index, the pop() method removes the last item. 
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# The del keyword also removes the specified index:
myList = ["apple", "orange", "kiwi"]
del myList[0]
print(myList)

# The del keyword can also delete the list completely. 
del myList


# Clear the List 
# The clear() method empties the list. The list still remains, but it has no content.
thislist.clear()
print(thislist) 
