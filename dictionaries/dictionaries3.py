# Copy
"""
We cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, 
 and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy, one way is to use the built-in Dictionary method copy().
"""

# Make a copy a dictionary with the copy() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# Another way to make a copy is to use the built-in function dict():
mydict = dict(thisdict)
print(mydict)



# Nested Dictionaries 
# A dictionary can contain dictionaries, this is called nested dictionaries. 

# Create a dictionary that contains three dictionaries:
myfamily = {
    "child1": {
        "name": "Jack",
        "year": 2026
    },
    "child2" : {
        "name": "Kate",
        "year": 2029
    },
    "child3" : {
        "name": "Jacob",
        "year": 2029
    }
}

print(myfamily)


# Or, if we want to add three dictionaries into a new dictionary:
child1 = {
    "name" : "Jack",
    "year" : 2026
}
child2 = {
    "name" : "Kate",
    "year" : 2029
}
child3 = {
    "name" : "Jacob",
    "year" : 2029
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)


# Acces Items in Nested Dictionaries
# To access items from a nested dictionary, we can use the name of the dictionaries, starting the outer dictionary:
print(myfamily["child2"]["name"])
print(myfamily["child1"]["year"])