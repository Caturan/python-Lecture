# We can change the value of a specific item by referring to its key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 1982

print(thisdict)


# Update Dictionary
"""
The update() method will update the dictionary with the items from the given argument. 
The argument must be a dictionary, or an iterable with key: value pairs. 
"""

car = {
    "brand": "Ferrari", 
    "model": "Rome",
    "year": 2021
}
car.update({"year": 2022})

print(car)


# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
car["color"] = "red"

print(car)


# Update Dictionary 
"""
The update() method will update the dictionary with the items from a given argument.
If the item does not exist, the item will be added. 
The argument must be a dictionary, or an iterable object with key: value pairs. 
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"}) 

print(thisdict)



# Removing Items
# There are several methods to remove items from a dictionary. 

# The pop() method removes the item with the specified key name:
thisdict.pop("color")
print(thisdict)


# The popitem() method removes the last inserted item:
thisdict = {
    "brand": "Volvo",
    "model": "XC90",
    "year": 2023
} 
thisdict.popitem()
print(thisdict)


# The del keyword removes the item with the specified key name: 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


# The del keyword can also delete the dictionary completely:
#del thisdict 
#print(thisdict)


# The clear() method empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1982
}
thisdict.clear()
print(thisdict)



# Loop
"""
We can loop through a dictionary by using a for loop. 
When looping through a dictionary, the return values are the keys of the dictionary, 
but there are methods to return the values as well. 
"""
thisdict = {
    "brand": "Mercedes",
    "model": "E63 AMG",
    "year": 2025
}

# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])


# We can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)


# We can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)


# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)