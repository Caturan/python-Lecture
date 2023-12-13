"""
    To write to an existing file, we must add a parameter to the open() function:
    "a" - Append - will append to the end of the file
    "w" - Write - will owerwrite any existing content
"""

f = open("demofile2.txt", "a")
f.write("Now the file has more content")
f.close()

# open and read the file after the appending:
f = open("demofile2.txt")
print(f.read())

f = open("demofile2.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

# Note: The "w" method will overwrite the entire file. 

# "x" - Create - will create a file, returns an error if the file exist
f = open("myfile.txt", "x")
f.read()