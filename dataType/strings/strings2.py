# Modify Strings

# Upper Case
# The upper() method returns the string in upper case:
a = "Hello World"
print(a.upper())


# Lower Case 
# The lower() method returns the string in lower case:
print(a.lower())
 

# Remove WhiteSpace
# Whitespace is the space before and/or after the actual text, and very often we want to remove this space. 
b = " Bonjour "
print(b)
print(b.strip())


# Replace String
# The replace() method replaces a string with another string:
print(b.replace("o", "a"))


# Split String
# The split() method returns a list where the text between the specified separator becomes the list items. 
a = "Hello, World!"
print(a.split(","))


# String Concatenation
# To concatenate, or combine, two strings we can use the + operator. 
a = "Hello"
b = "World"
c = a + b
print(c)

c = a+ " " + b
print(c)
