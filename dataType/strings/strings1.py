"""
Strings

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""


# Multiline Strings 
a = """ sdfsgsfafsdg
dfgsdgdfghdfhfg
dfgsgfgh"""
print(a)


"""
    String are Arrays
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""

a = "Hello Python"
print(a[1])


# Since strings are arrays, we can through the characters in a string, with a for loop. 
for x in "banana":
    print(x)


# To get the length of a string, use the len() function. 
a = "Hello World"
print(len(a))


# Check string
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



        
# Slicing 
# We can return a range of characters by using the slice syntax. 

b = "Hello, world"
print(b[2:5])

# The first character has index 0. 

b = "Hello"
print(b[:5])

b = "World"
print(b[3:])



