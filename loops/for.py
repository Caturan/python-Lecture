# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc. 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)


# break Statement
# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Exit the loop when x is "banana", but this time the break comes before the print:
for x in fruits:
    if x == "banana":
        break
    print(x)


# The continue statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
for x in fruits:
    if x == "banana":
        continue
    print(x)


# The range() Function
"""
To loop through a set of code a specified number of times, we can use the range() function,
the range() functions returns a sequence of numbers, starting from 0 from by default, and increments by 1 and ends at specified number.
"""
for x in range(6):
  print(x)

# The range() function is possible to specift the startig values by adding a parameter: range(2, 6)
for x in range(2, 6):
    print(x)

"""
The range() function defaults to increment the sequence by 1, 
howewer it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
"""
for x in range(2, 30, 3):
    print(x)


# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")


# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
    

# Nested Loops
# A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 


# The pass Statement
"""
for loops cannot be empty, but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error.
"""
for x in [0, 1, 2]:
    pass

