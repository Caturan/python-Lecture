"""
    Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    Mat size must be 

    X. ( is an odd natural number, and is times
    .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Input

    9 27

Sample Output

    ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------

"""

def generate_door_mat(rows, columns):
    # Generate the upper part of the door mat
    for i in range(rows//2):
        pattern = '.|.' * (2*i + 1)
        print(pattern.center(columns, '-'))

    # Print the "WELCOME" line
    print('WELCOME'.center(columns, '-'))

    # Generate the lower part of the door mat
    for i in range(rows//2 - 1, -1, -1):
        pattern = '.|.' * (2*i + 1)
        print(pattern.center(columns, '-'))

# Read input from STDIN
row_column = input()
rows, columns = map(int, row_column.split())

# Generate door mat pattern
generate_door_mat(rows, columns)
