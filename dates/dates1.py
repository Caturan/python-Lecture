import datetime

"""
Python Dates
A date in Python is not a data type of its own, but we can import a module named 
datetime to work with dates as date objects. 
"""
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))


"""
Creating Date Objects 
To create a date, we can use the datetime() class (constructor) of the datetime module. 
The datetime() class requires three parameters to create a date: year, month, day. 
"""
x = datetime.datetime(2015, 5, 19)
print(x)
"""
The datetime() class also takes parameters for time and timezones, 
but they are optional, and has a default value of 0. 
"""

"""
The strftime() Method
The datetime object has a method for something date objects into readable strings. 
And takes one parameter, format, to specify the format of the returned string:
"""
print(x.strftime("%B"))


