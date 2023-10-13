# Python supports the usual logical conditons from mathematics

a = 33
b = 200 
if b > a:
    print("b is greater than a")


# Elif
# The elif keyword is Pytohns' way of saying "if the previous conditons were not true, then try this condition".

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


# Else 
# The else keyword catches anything which isn't caought by the preceding conditons. 
a = 200
b = 33

if b >  a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# If we have onyl one statement to execute, we can put it on the same line as the if statement. 
if a > b: print("a is greater than b")


# If we have only one statement to execute, one for if, and one for else, we can put it all on the same line:
print("a") if a > b else print("b")


a = 2 
b = 300
print("a") if a > b else print("b")


# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditonal statements:
a = 200 
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditonal statements:
if a > b or a > c:
    print("At least one of the conditions is True") 


# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statemet:
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")


# Nested If
# We can have if statements inside if statements, this is called nested if statements:
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# The pass Statement
"""
if statements cannot be empty, but if we for some reason have an if statement with no content, 
put in the the pass statement to avoid getting an error. 
"""
a = 33
b = 200

if b > a:
    pass


