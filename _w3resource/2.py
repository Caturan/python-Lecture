# Write a Python program to find out what version of Python you are using

import sys  # Import the sys module to access system-specific parameters and functions

# Print the Python version to the console
print("Python version")

# Use the sys.version attribute to get the Python version and print it
print(sys.version)

# Print information about the Python version
print("Version info.")

# Use the sys.version_info attribute to get detailed version information and print it
print(sys.version_info)

"""
Check the Python version on command line:

user@machine1:~$ python --version
Python 2.7.17
user@machine1:~$ python -V
Python 2.7.17
user@machine1:~$ python3 --version
Python 3.6.9
user@machine1:~$ python3 -V
Python 3.6.9 
"""

# Using platform module
import platform
print(platform.python_version())
