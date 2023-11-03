import asyncio

    # Coroutines and Concurrency with asyncio
"""
    Coroutines:
Coroutines are a way to write asynchronus code in Python. They are a special type of function that can yield control back to the event loop, 
allowing other tasks to run in the meantime. 
Coroutines are defined using the 'async' keyword, and we can use the 'await' keyword within them to pause their execution until a certain task is complete.
"""

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello())
"""
In this example, 'asyncio.sleep(1)' is a non-blocking operation that pauses the 'hello()' coroutines for 1 second, 
allowing other tasks to run in the meantime. 
"""

# print(dir(asyncio))

"""
    Concurrency with asyncio:
Asyncio is a Python library for writing asynchronous code using corotuines. 
It allow us to write concurrent code that can perform multiple I/O-bound tasks without blocking the main thread. 
Here's a basic example of how asyncio can be used for concurrent tasks: 
"""

async def task1():
    await asyncio.sleep(1)
    print("Task 1 complete")

async def task2():
    #await asyncio.sleep(2)
    print("Task 2 complete")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())


"""
Asyncio also provides event loops and various utilites for handling I/O-bound operation, 
making it well-suited for tasks like network request, file I/O, and other asynchronous operations. 

Keep in mind that asyncio is most benefical when dealing with I/O-bound operations. If we have CPU-bound tasks, 
we might want to use multithreading or multiprocessing instead, as asyncio's event loop runs in a single thread. 
"""

