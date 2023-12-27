        # Pooling between process
"""
def square(n):
    return(n*n)

if __name__ == "__main__":
    mylist = [1,2,3,4,5]
    result = []
    for num in mylist:
        result.append(square(num))

    print(result)
"""
"""
    It is a simple program to calculate squares of elements of a given list. In  a multi-core/multi-processor system. 
    Only one of the cores is used for program execution and it's quite possible that other cores remain idle. 
"""

"""
Pooling between processes:
    In order to utilize all the cores, multiprocessing module provides a Pool class. 
    The Pool class represents a pool of worker processes. It has methods which allows tasks to be offloaded to the worker processes in a few different ways. 
"""
import multiprocessing
import os 

def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return (n*n)

if __name__ == "__main__":
    mylist = [1,2,3,4,5]
    
    p = multiprocessing.Pool()
    
    result = p.map(square, mylist) 
    print(result)

