# String Format 
""" As we learned in the Python Variables chapter, we cannot combine and numbers with plus. 
But we can combine strings and numbers by using the format() method. 
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are: 
""" 

age = 22
txt = "My name is Ahmet, and I am {}"
print(txt.format(age))


queantity = 3 
itemno = 523
price = 25.5
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(queantity,itemno,price)) 


myOrder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myOrder.format(queantity,itemno,price)) 



# Escape Character 
"""
To insert characters that are illegal in a string, use an escape character. 
An escape character is a backslash \ followed by the character we want to insert. 
An example of an illegal character is a double quote inside a string that is surrounded by double quotes: 
"""

txt = "We are the so-called \"Vikings\" from the north." 
print(txt)