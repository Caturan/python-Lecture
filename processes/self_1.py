
"""
What is multiprocessing?
    Multiprocessing refers to the ability of a system to support more than one processor at the same time. 
    Applications in a multiprocessing system are broken to smaller routines that run independently. 
    The operating system allocates these threads to the processor improving performance of the system. 
"""

"""
Why multiprocessing?
    The more tasks we must do at once, the more dificult it gets to keep track of them all, and keeping the timing right becomes more of a challenge. 
    This is where the concept of multiprocessing arises!
    A multiprocessing system can have:
    - multiprocessor, i.e. a computer with more than one central processor. 
    - multi-core processor, i.e. a single computing component with two or more independent actual processing units (called "cores")
    Here, the CPU can easily executes several tasks at once, with each task using its own processor. 
"""

import multiprocessing

def print_cube(num):
    print("Cube: {}".format((num * num * num)))

def print_square(num):
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!")


"""
    To create a process, we create an object of Process class. It takes following arguments:
    - target: the function to be executed by process
    - args: the arguments to be passed to the target function
"""


print()
# Another example
import multiprocessing
import os 

def worker1():
    print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
    print("ID process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
    print("ID of main process: {}".format(os.getpid()))

    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    p1.start()
    p2.start()

    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    p1.join()
    p2.join() 

    print("Both of ended")

    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))

    