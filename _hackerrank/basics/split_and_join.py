"""
     You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. 
"""

def split_and_join(line):
    a = line
    a = a.split(" ")
    a = "-".join(a)
    return a
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)