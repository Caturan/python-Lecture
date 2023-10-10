# Unpack Tuples

"""
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
"""

fruits = ("apple", "banana", "cherry")

# But in Python, we are also allowed to extact the values back into variables. This is called "unpacking":

# Unpacking Tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# Using Asterisk *
"""
If the number of variables is less than the number of values,
we can add an *  to the variable name and the values will be assigned to the variable as a list:
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


"""
If the asterisk is added to another variable name than the last, 
Python will assign values to the variable until the number of values left matches the number of variables left.
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)



# Loop Throug a Tuple
# We can loop through the tuple items by using a for loop. 
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(i, thistuple[i])



# Join Two Tuples
# To join two or more tuples we can use the + operator:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Multiply Tuples
# If we want to multiply the content of a tuple a given number of times, we can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# Tuple Methods
# Python has two built-in methods that we can use on tuples. 
count() # Returns the number of times a specified value occurs in a tuple
index() # Searches the tuple for a specified value and returns the position of where it was found. 
 