    # Coroutines
"""
    Coroutines are a generalization of subroutines(functions) used for cooperative multitasking. 
    Unlike functions that return once and do not maintain state, coroutines can pause their execution and later continue from where they left off. 
"""
import time 
import asyncio

# traditional function
def my_function():
    print("Start of the function")
    time.sleep(1)
    print("End of the function")

# coroutine
async def my_coroutine():
    print("Start of the coroutine")
    await asyncio.sleep(1)
    print("End of the coroutine")

my_function()
asyncio.run(my_coroutine())


"""
    The performance improvement comes from awaiting more than one coroutime. 
    So we can start more than one coroutine at once to solve multiptle IO-bound problems, such as fetching some data, reading some files, etc.  
"""
async def coroutine_1():
    print("Start of coroutine_1")
    await asyncio.sleep(1)
    print("End of coroutine_1")

async def coroutine_2():
    print("Start of coroutine_2")
    await asyncio.sleep(1)
    print("End of coroutine_2")

async def main():
    coroutines = [coroutine_1(), coroutine_2()]
    await asyncio.gather(*coroutines)

asyncio.run(main())


"""
Awaitable Class
    Like naming functions as callables, the term awaitable is introduced with coroutines. 
    Therefore similar to defining __call__ method of a class to make it callable, we define __await__ method of a class to make it awaitable. 
    We can call these type of classes directly, or we can create an object from them. 
"""
class AwaitableClass:
    def __await__(self):
        print("Awaiting")
        yield
        print("Done")

async def main():
    print("Starting main")
    await AwaitableClass()
    awaitable_object = AwaitableClass()
    await awaitable_object
    awaitable_object = AwaitableClass()
    await awaitable_object
    print("Ending main")

asyncio.run(main())
