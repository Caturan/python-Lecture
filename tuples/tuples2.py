# Acces Tuple Items
"""
We can access tuple items by referring to the index number, inside square brackets.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


# Also we can use the negative indexing. 

# Range of Indexes
"""
We can specify a range of indexes by specifying where to start and where to end the range. 
When specifying a range, the return value will be a new tuple with the specified items. 
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])



# Check if item Exists
# To determine if a specified item is present in a tuple use the in keyword:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple is in the tuple.")



# Python - Update Tuples
"""
Tuples are unchangeable, meaning that we cannot change, add or remove items once the tuple is created. 
But there are some workarounds.
"""

# Convert the tuple into a list to be able to change it:
x = ("apple", "cherry", "banana")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# Add Items
"""
Since tuples are immutable, they do not have a built-in append() method,
 but there are other ways to add items to a tuple. 
"""

"""
1. Convert into a list: Just like the workaround for changing a tuple, we can convert it into a list,
add our item(s), and convert it back to into a tuple. 
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


"""
2. Add tuple to a tuple. We are allowed to add tuples to tuples, so if we want to add one item, (or many),
create a new tuple with the item(s), and add it to the existing tuple:
"""
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)


# Remove
"""
Convert the tuple into a list, remove "apple", and convert it back into a tuple:
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)


# Or we can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)

