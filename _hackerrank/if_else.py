import math

"""
Given an integer, n, perform the following conditional actions:
- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5, print Not Weird
- If n is even and in the inclusive range of 6 to 20, print Weird
- If n is even and greater than 20, print Not Weird
- 1<=n<=100
"""

if __name__ == '__main__':
    print("Please input a positive integer smaller than 100: ")
    n = int(input().strip())

    if 1 <= n <= 100:     
        if n % 2 != 0:
            print("Weird")
        elif n % 2 == 0 and 2 <= n <= 5:
            print("Not Weird")
        elif n % 2 == 0 and 6 <= n <= 20:
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")
    else: 
        print("The input is not within the specified range (1 to 100) ")
    