
"""
Using Locks:
    multiprocessing module provides a Lock class to deal with the race conditions. 
    Lock is implemented using a Semaphore object provided by the Operating System. 

    A semaphore is a synchronization object that controls access by multiple processes to a common resource in a parallel programming environment. 
    It is simply a value in a designated place in operating system (or kernel) strage that each process can check and then change. 
    Depending on the value that is found, the processes can use the resource or will find that it is already in use and must wait for some period before trying again. 

    Semapphores can be binary (0 or 1) or can have additional values. Typically, a process using semophores checks the value and then, if it using the resource, 
     changes the value to reflect this so that subsequent semaphore users will know to wait. 
"""

import multiprocessing

def withdraw(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

def deposit(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def perform_transactions():
    balance = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=withdraw, args=(balance,lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Final balance = {}".format(balance.value))

if __name__ == "__main__":
    for _ in range(10):
        perform_transactions()

"""
    In the critical section of target function, we apply lock using lock.acquire() method. 
    As soon as a lock is acquired, no other process can access its critical section until the lock is released using lock.release() method. 
"""
