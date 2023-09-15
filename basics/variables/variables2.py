#       Variable Names
"""
Rules for Python variables: 
1-) A variable name must start with a letter or the underscore character. 
2-) A variable name cannot start with a number. 
3-) A variable name can only contain alpha-numeric characters and underscores. 
4-) Variable names are case sensitive (age, Age, AGE are three different variables)
5-) A variable name cannot be any of the Python keywords. 
"""

#       Multi Words Variable Names 
# There are several techniques we can use to make them more readable:

# camelCase (Each word, except the first, starts with a capital letter)
myVariableName = "Jack"

# PascalCase (Each word starts with a capital letter):
MyVariableName = "Jack"

# snake_case (Each word is seperated by an underscore character):
my_variable_name = "Jack"




#       Asssign Multiple Values

# Python allows you to assign values to multiple variables in one line: 
"""
x, y, z = "Orange" "Banana", "Cherry"
print(x)
print(y)
print(z)
"""   # In there we need to unpack 

# And we can assign the same value to multiple variables in one line:
q = w = e = "Orange"
print(q)
print(w)
print(e)


#  IF we have a calloction of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.  
fruits = ["apple", "banana", "cherry"] 
a, s, d = fruits
print(a)
print(s)
print(d)
