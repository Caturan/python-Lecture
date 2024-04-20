"""
    The first line contains an integer, , denoting the number of commands.
    Each line of the subsequent lines contains one of the commands described above.

    Constraints
        The elements added to the list must be integers.

    Output Format  
        For each command of type print, print the list on a new line.

    Sample Input:
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

    Sample Output:
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
"""

if __name__ == '__main__':
    import re
    N = int(input())
    k = []
    for i in range(N):
        a = str(input())
        b = re.split('\s',a)
        if b[0] == 'insert':
            z = int(b[1])
            x = int(b[2])
            k.insert(z,x)
        elif b[0] == 'print':
            print(k)
        elif b[0] == 'remove':
            y = int(b[1])
            k.remove(y)
        elif b[0] == 'append':
            v = int(b[1])
            k.append(v)
        elif b[0] == 'sort':
            k.sort()
        elif b[0] == 'pop':
            k.pop()
        elif b[0] == 'reverse':
            k.reverse()
        

