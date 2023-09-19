# Boolean Values

# When we compare two values, the expression is evaluted and Python returns the Boolean answer: 

print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 100 
b = 32

if b > a:
    print("b is greater than a")
else: 
    print("b is not greater than a")


# The bool() function allow us to evaluate any value, and give us True or False in return :
 
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


"""
Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
And the value False evalluates to False
"""

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# We can create functions that returns a Boolean Value:
def myFunction() :
    return True
print(myFunction())


if myFunction():
    print("YES")
else:
    print("NO")


# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))