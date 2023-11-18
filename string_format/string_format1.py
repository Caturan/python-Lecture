"""
    String Formatting
To make sure a string will display as expected, we can format the result with the format() method.
The format() method allows us to format selected parts of string. 
Sometimes there are parts of a text that we do not control, maybe they come from a database, or user input? 
To control such values, add placeholders (curly brackets {}) in the text, and run the values throught the format() method. 
"""
price = 49 
txt = "The price is {} dollars"
print(txt.format(price))


# We can add parameters inside the curly brackets to specify how to convert the value:
txt = "The price is {:.2f } dollars"

"""
    Multiple Values
If we want to use more values, just add more values to the format() method:
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(quantity, itemno, price))

"""
    Index Numbers
We can use index numbers to be sure the values are placed in the correct placeholders:
"""
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars"
print(myorder.format(quantity, itemno, price))

# Also, if we want to refer to the same value more than once, use the index number:
age = 22
name = "Jack"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


"""
    Named Indexes
We can also use named indexes by entering a name inside thte curly brackets, 
 but then we must use names when we pass the parameter values:
"""
myorder = "I have a {carname}, it is a {model}"
print(myorder.format(carname = "Ford", model = "Mustang"))