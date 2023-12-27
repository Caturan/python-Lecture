
"""
Server Process:
    Whenever a python program starts, a server process is also started. 
    From there on, whenever a new process is needed, the parent process connects to the server and request it to fork a new process. 
    
    A server process can hold Pytohn objects and allows other processes to manipulate them using proxies. 
    multiprocessing module provides a Manager class which controls a server process. Hence, managers provide a way to create data that can be shared between different processes. 

    Server process managers are more flexible than using shared memory objects because they can be made to support arbitrary object types like:
     lists, dictionariesi Queue, Value, Array, etc 
    Also, a single manager can be shared by processes on different computers over a network. They are, however, slower than using shared memory. 
"""

import multiprocessing

def print_records(records):
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))

def insert_record(record, records):
    records.append(record)
    print("New record added!\n")

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        records = manager.list([('Sam',10), ('Adam', 9), ('Kevin', 9)])
        new_record = ('Jeff', 8)

        p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
        p2 = multiprocessing.Process(target=print_records, args=(records,))

        p1.start()
        p1.join()

        p2.start()
        p2.join()
"""
Let us try understand above piece of code:
    - First of all, we create a manager object using
    with multiprocessing.Manager() as manager:
    All the lines under with statement block are under the scope of manager object. 

    - Then we create a list records in server process memory using:
    records = manager.list([('Sam',10), ('Adam', 9), ('Kevin', 9)])

    -  Finally we create to processe p1(to insert a new record in records list) 
     and p2(to print records) and run them while passing records as one of the arguments. 

"""

"""
    Effective use of multiple processes usually requires some communication between them, 
    so that work can be divided and results can be aggregated multiprocessing supports two types of communication channel between processes: 
    - Queue
    - Pipe
"""
"""
    1. Queue: A simple way to communicate between process with multiprocessing is to use a Queue to pass messages back and forth. 
    Any Python object can pass through a Queue. 
"""
import multiprocessing

def square_list(mylist, q):
    for num in mylist:
        q.put(num * num)
        

def print_queue(q):
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue is now empty")

if __name__ == "__main__":
    mylist = [1,2,3,4]

    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()


"""
2. Pipes:
    A pipe can have only two endpoints. Hence, it is preferred over queue when only two-way communication is required. 
    multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe. 
    The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has send() and recv() methods (among others). 
"""
print()
import multiprocessing

def sender(conn,msgs):
    for msg in msgs:
        conn.send(msg)
        print("Sent the messge: {}".format(msg))
    conn.close()

def receiver(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":  # good trick
            break
        print("Received the message: {}".format(msg))

if __name__ == "__main__":
    msgs = ["hello", "hey", "hru?", "END"]

    parent_conn, child_conn = multiprocessing.Pipe() # A pipe create

    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

"""
Note: Data in a pipe may become corrupted if two processes (or threads) try to read from or write to the same end of the pipe at the same time. 
    Of course, there is no risk of corruption from processes using different ends of the pipe at the same time. 
    Also note that Queues do proper synchronization between processes, at the same time. 
    Also note that Queue do proper synchronization between processes, at the expence of more complexity. Hence, queues are said to be thread and process safe!
"""

