"""
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

girdi = input("Please input your data seperated with comma : ")


num_list = girdi.split(',')
num_tuple = tuple(num_list)


print("List:", num_list)
print("Tuple:", num_tuple)
