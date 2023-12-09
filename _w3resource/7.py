"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

ext = input("")
f_name = ext.split(".")

print(f_name[-1])