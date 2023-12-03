import threading
import time

#print(dir(threading))
#help(threading)

"""
    Python programs that we write run as a main thread. 
    threading module enables us to create extra threads. Let's see how we can create our threads. 
"""

''' From a Function: The easiest way to create a thread is using a function. '''
def thread_1():
    print(
        f"This is a thread created from a function "
        f"with id {threading.get_native_id()} "
    )

t = threading.Thread(target=thread_1)
t.start()


''' From a Class: On the other hand, the best practice is to create a thread from a class, which extends Thread class from threading module. '''
class Thread2(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print(
            f"This is a thread created from a class "
            f"with id {threading.get_native_id()}"
        )

t = Thread2()
t.start()

"""
Passing Arguments to Thread: 
    If we want to pass some arguments to our function while creating our thread, 
    we can use keyword argument args of Thread class. Notice the trick that to keep a single values as a tuple, we end the expression with a comma , .
"""
def thread_3(s):
    print(
        f"This is a thread created from a function "
        f"with id {threading.get_native_id()} "
        f"and your argument is {s}"
    )

t = threading.Thread(target=thread_3, args=("Thread 3",))
t.start()

print()


"""
Scheduling with start/join
    Similar to await that we have learned for coroutines,
     we can wait the ending of thread by using join method. 
"""
def thread_4_1():
    print(f"This is thread 4_1 with id {threading.get_native_id()}")
    time.sleep(1)
    print(f"Thread 4_1 is done")

def thread_4_2():
    print(f"This is thread 4_2 with id {threading.get_native_id()}")
    time.sleep(3)
    print(f"Thread 4_2 is done")

def thread_4_3():
    print(f"This is thread 4_3 with id {threading.get_native_id()}")
    print(f"I can only start after thread 4_1 and thread 4_2 are done")
    time.sleep(1)
    print(f"Thread 4_3 is done")

t1 = threading.Thread(target=thread_4_1)
t2 = threading.Thread(target=thread_4_2)
t3 = threading.Thread(target=thread_4_3)
t1.start()
t2.start()
t1.join()
t2.join()
t3.start()

print()

def thread_5():
    print(f"This is a daemon thread with id {threading.get_native_id()}")
    while True:
        time.sleep(1)
        print(f"I am still alive because I am a daemon thread")
    print(f"I will never be printed because I am a daemon thread")

def thread_6():
    print(f"This is a non-daemon thread with id {threading.get_native_id()}")
    time.sleep(10)
    print(f"I am done therefore the program will exit")

t1 = threading.Thread(
    target=thread_5
)  # or t1 = threading.Thread(target=thread_5, daemon=True)
t2 = threading.Thread(target=thread_6)
t1.daemon = True
t1.start()
t2.start()