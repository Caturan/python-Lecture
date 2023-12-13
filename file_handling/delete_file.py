
# To delete a file, we must import the OS module, and run its os.remove() function:

import os
os.remove("demofile2.txt")


"""
    Check if File exist:
    To avoid getting an error, we might want to check if the file exists begore we try to delete it: 
"""

if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("The file does not exist")


# To delete an entire folder, use the os.rmdir() method. 
# We can only remove empty folders. 

