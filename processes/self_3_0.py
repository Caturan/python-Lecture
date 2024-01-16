
""" 
    This article discusses two important concepts related to multiprocessing in Python:
    - Synchronization between processes
    - Pooling of processes
"""

"""
Synchronization between processes:
    Process synchronization is defined as a mechanism which ensures that two or more concurrent process do not simultaneously execute, 
     some particular program segment known as critical section. 
    
    Critical section refers to the parts of the program where the shared resource is accessed. 

    Concurrent accesses to shared resource can lead to race condition. 
    A  race condition occurs when two or more processes can access shared data and try to change it at the same time. 
    As a result, the values of variables may be unpredictable and vary depending on the timings of context switches of the processes. 
"""

import multiprocessing

def withdraw(balance):
    for _ in range(10000):
        balance.value = balance.value - 1

def deposit(balance):
    for _ in range(10000):
        balance.value = balance.value + 1

def perform_transactions():
    balance = multiprocessing.Value('i', 100)


    p1 = multiprocessing.Process(target=withdraw, args=(balance,))
    p2 = multiprocessing.Process(target=deposit, args=(balance,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final balance = {}".format(balance.value))

if __name__ == "__main__":
    for _ in range(10):
        perform_transactions()

"""
    The expected final balance is 100 but what we get in 10 iterations of perform_transaction function is some different values. 
    This happens due to concurrent access of processes to the shared data balance. This unpredictablity in balance value is nothing but race condition. 
"""
