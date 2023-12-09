"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math
r = float(input())

pi = math.pi

circle_area = ((pi)* (r*r)) 
print("Circle area is: ", circle_area)