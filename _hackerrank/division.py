
"""
The provided code stub reads two integers, a and b, from STDIN
Add logic to print two lines. The first line should contain the result of integer division, a // b. 
The second line should contain the result of float divison a / b.  
No rounding or formartting is necessary. 
"""

a = int(input().strip())
b = int(input().strip())

result1 = a // b
result2 = a / b 

print(result1)
print(result2)