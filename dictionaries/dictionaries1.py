# Dictionaries

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Dictionaries are used to store data values in key: value pairs
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:

print(thisdict)

# Dictionaries items are presented in key: values pairs, and can be referred to by using the key name. 

print(thisdict["brand"])


# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created. 


# Dictionaries cannot have two items with the same key:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print(thisdict)


# With len() func we can know how many items:
print(len(thisdict))

# The values in dictionary items can be of any data type:

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 

print(thisdict)


# From Python's perspective, dictionaries are defined as objects with the data type 'dict':
print(type(thisdict))



# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary. 
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# We can access the items of a dictionary by referring to its key name, inside square brackets:
print(thisdict["country"])

# There is also a method called get() that will give us the same result:
print(thisdict.get("name"))



# Get Keys
# The keys() method will return a list of all the keys in the dictionary. 
print(thisdict.keys())


car = {
    "brand": "Ferrari",
    "model": "Roma",
    "year": 2021
}

x = car.keys()

print(x) # before the change

car["color"] = "black"

print(x)


# Get Values
# The values() method will return a list of all the values in the dictionary. 
x = car.values()
print(x)

# Make a change in the originial dictionary, and see that the values lists gets updated as well:
car["year"] = 2022

print(x)



# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
x = car.items()
print(x)



# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one og the keys in the dictionay:", thisdict["model"])

