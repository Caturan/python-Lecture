import asyncio

"""
    Q1: Write a Python program that creates an asynchronous function to print "Python Exercises!" with a two second delay
"""
async def ex():
    await asyncio.sleep(2)
    print("Python Exercises!")

async def main():
    await ex()

asyncio.run(main())


"""
    Q2: Write a Python program that creates three asynchronous functions and displays their respective names with different delays (1 second, 2 seconds, and 3 second)
"""

async def display_name_with_delay(name, delay):
    await asyncio.sleep(delay)
    print(name)
async def main():
    tasks = [
        display_name_with_delay("Asyn. function-1", 1),
        display_name_with_delay("Asyn. function-2", 2),
        display_name_with_delay("Asyn. function-3", 3)
    ]    
    await asyncio.gather(*tasks)

asyncio.run(main())


"""
   Q3: Write a Python program that creates an asyncio event loop and runs a coroutine that prints numbers from 1 to 7 with a delay of 1 second each. 
"""
async def delay_number():
    for i in range(7):
        print(i+1)
        await asyncio.sleep(1)

asyncio.run(delay_number())


"""
    Q4: Write a Python program that runs multiple asynchronous tasks concurrently using asyncio.gather() and measures the time taken. 
"""
import time

async def coroutine_1():
    print("C1 start")
    await asyncio.sleep(2)
    print("C1 end")

async def coroutine_2():
    print("C2 start")
    await asyncio.sleep(2)
    print("C2 end")

async def coroutine_3():
    print("C3 start")
    await asyncio.sleep(4)
    print("C3 end")

async def main():
    start_time = time.time()
    corutines = [coroutine_1(), coroutine_2(), coroutine_3()]
    await asyncio.gather(*corutines)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

asyncio.run(main())




