
"""
The included code stub will read an nteger, n, from STDIN
Without using any string methods, try to print the following:
123...n
Note that "..." represent the consecutive values in between 
"""

def _printfunc(n):
    output = ""
    while 1 <= n <= 150:
        output = str(n) + output 
        n -= 1
    print(output)

if __name__ == "__main__":
    n = int(input())
    _printfunc(n)




