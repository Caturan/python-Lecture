
"""
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2
"""
print("Please input a positive integer: ")
n = int(input().strip())

i = 0
while i < n:
    print(i**2)
    i+=1

