
"""
Creating Process:
    Fork: Creates a new process by duplicating the current process. 
    The new process (child) is an exact copy of the parent process at the point of creation. 
    It shares the same memory space and context. 
    - Faster start-up time, because no need to initialize a new interpreter. 
    - Memory efficiency, due to shared resources at the point of working. 
    - Can lead to issues in multi-threaded programs, as threads are not safely forked. 

    Spawn:
    Starts a fresh Python interpreter process. 
    The child process is only given access to the resources that are explicitly passed to it by the parent process. 
    - Safer and more predictable, especially for multi-threaded applications. 
    - Better compatibility across different platforms like Linux / Mac / Windows. 
    - Slower start-up time and higher memory usage.   
"""

import threading
import multiprocessing
import os
import time


# Creting Processes with Pass Arguments
def process_3(s):
    print(
        f"This is a process created from a function "
        f"with id {os.getpid()} "
        f"and your argument is {s}"
    )
    time.sleep(5)

def main():
    p = multiprocessing.Process(target=process_3, args=("Process3",))
    p.start()


# Creating Processes from Class
class Process2(multiprocessing.Process):
    def __init__(self):
        super().__init__()
    
    def run(self):
        print(f"This is a process created from a class with id {os.getpid()}")
        time.sleep(5)

def main_2():
    p = Process2()  
    p.start()


# Synchronisation
def process_4_1():
    print(f"This is process 4_1 with id {os.getpid()}")
    time.sleep(1)
    print(f"Process 4_1 is done")

def process_4_2():
    print(f"This is process 4_2 with id {os.getpid()}")
    time.sleep(3)
    print(f"Process 4_2 is done")

def process_4_3():
    print(f"This is process 4_3 with id {os.getpid()}")
    print(f"I can only start after process 4_1 and process 4_2 are done")
    time.sleep(1)
    print(f"Process 4_3 is done")

def main_3():
    p1 = multiprocessing.Process(target=process_4_1)
    p2 = multiprocessing.Process(target=process_4_2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    p3 = multiprocessing.Process(target=process_4_3)
    p3.start()
    print(f"Process 4 is done")


if __name__ == "__main__":
    multiprocessing.freeze_support()

    main()
    main_2()
    main_3()



   