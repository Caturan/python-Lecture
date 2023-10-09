# Loop Through a List
# We can loop through the list items by using a for loop. 

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)



# We can also loop through the list items by referring to their index number. 
# Use the range() and len() functions to create a suitable iterable. 
for i in range(len(thislist)):
    print(i, thislist[i])


# List Comprehension offers the shortest syntax for looping through lists:
[print(x) for x in thislist]


"""
List comphrehension offers a shorter syntax when we want create a new list based on the values of an existing list.
Exapmle:
Based on a list of fruits, we wnat a new list, containing only the fruits with the letter "a" in the name. 
Without list comprehension we will have to write a for statement with a conditional test inside: 
"""
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension we can do all that with only one line of code:
newlist = [x for x in fruits if "a" in x]
print(newlist)


# Condition
# The condition is like a filter that only accepts the items that value to True
newlist = [x for x in fruits if x != "apple"]
print(newlist)


# We can use the range() function to create an iterable:
mylist = [x for x in range(10)]
print(mylist)

# Accept only numbers lower than 5: 
mylist = [x for x in range(10) if x < 5]
print(mylist)

# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

# We can set the outcome to whatever we like:
mylist = ['hello'  for x in fruits]
print(mylist)



# Sort List Alphanumerically 
# List objects have a sort() method that will sort the list alphanumerically, ascending: 
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


mylist = [102, 42, 64, 96, 21]
mylist.sort()
print(mylist)

# To sort descending, use the keyword argument reverse = True:
mylist.sort(reverse=True)
print(mylist)


# Customize Sort Function
"""
We can also customize our own function by using the keyword argument key = function. 
The function will return a number that will be used to sort the list (the lowest number first)
"""
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# By default sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) 


""" 
Luckilly we can use built-in functions as key functions when sorting a list. 
So if we want a case-insensitive sort function, use str.lower as a key function:
"""
thislist.sort(key = str.lower)
print(thislist)



# Reverse Order
"""
What if we want to reverse the order of a list, regardless of the alphabet? 
The reverse() method reverses the current sorting order of the elements. 
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



# Copy a List
"""
We cannot copy a list simply by typing list2 = list1, because list2 will only be a reference to list1,
 and changes made in list1 will automatically also be made in list2. 
"""
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list()
mylist2 = list(mylist)
print(mylist2)



# Join Two Lists
"""
There are several ways to join, or concatenate, two or more lists in Python. 
One of the easist ways are by using the + operator. 
"""
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 


# Another way to join lists is by appending all the items from list2 into list1, one by one: 
for x in list2:
    list1.append(x)

print(list1)


# Or we can use the extend() method, where the purpose is to add elements from one list to another list: 
list1.extend(list2)
print(list1)