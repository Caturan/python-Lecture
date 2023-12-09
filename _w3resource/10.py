"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

a = int(input())
print(a + (10*a + a) + (100*a + 10*a+a))

# Another way of solution: 
n1 = int("%s" % a)          # Convert 'a' to an integer
n2 = int("%s%s" % (a, a))   # Concatenate 'a' with itself and convert to an integer
n3 = int("%s%s%s" % (a, a, a))  # Concatenate 'a' with itself twice and convert to an integer

# Calculate the sum of 'n1', 'n2', and 'n3' and print the result
print(n1 + n2 + n3)