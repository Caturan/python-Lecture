
"""
    File handling is an important part of any web application. 
    Python has several functions for creating, reading, updating, and deleting files. 
"""

"""
    File Handling:
    The key function for working with files in Python is the open() function. 
    The open() function takes two parameters; filename and mode. 
    
    There are four different methods (modes) for opening file:
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist

    "a" - Append - Opens a file for appending, creates the file if it does not exist

    "w" - Write - Opens a file for writing, creates the file if it does not exist

    "x" - Create - Creates the specified file, returns an error if the file exists

    In addition we can specify if the file should be handled as binary or text mode. 
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode 
"""

f = open("demofile.txt")

f = open("demofile.txt", "rt")

# The open() function returns a file object, which has a read() method for reading content of the file: 
print(f.read())

# If the file is located in a different location, we will have to specify the file paths. 


"""
    By default the read() method returns the whole text, but we can also specify how many characters we want to return. 
"""
f = open("demofile.txt")
print(f.read(5))

# We can return one line by using the readline() method: 
f = open("demofile.txt")
print(f.readline())

# By calling readline() two times, we can read the two first lines:
f = open("demofile.txt")
print(f.readline())
print(f.readline()) 

# By looping through the lines of the file, we can read the whole file, line by line:
f = open("demofile.txt")
for x in f:
    print(x)

# Close Files
"""
    It is a good practice to always close the file when we are done with it. 
"""
f.close()
#print(f.read())

