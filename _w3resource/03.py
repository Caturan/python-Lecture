"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
"""

"""
Python datetime:

The datetime module supplies classes for manipulating dates and times in both simple and complex ways. datetime.now(tz=None) returns the current local date and time.
If optional argument tz is None or not specified, this is like today().
"""

# Import the 'datetime' module to work with date and time
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Create a datetime object representing the current date and time

# Display a message indicating what is being printed
print("Current date and time : ")

# Print the current date and time in a specific format
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Use the 'strftime' method to format the datetime object as a string with the desired format


