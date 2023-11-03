import asyncio
import time

def function_1():
    print("F1: Starting function")
    time.sleep(5)  
    print("F1: Ending function")

def function_2():
    print("F2: Starting function")
    time.sleep(2)
    print("F2: Ending function")


def sync_main():
    print("Sync: Starting main")
    function_1()
    function_2()
    print("Sync: Ending main")


async def coroutine_1():
    print("C1: Start")
    await asyncio.sleep(5)
    print("C1: End")


async def coroutine_2():
    print("C2: Start")
    await asyncio.sleep(2)
    print("C2: End")

async def async_main():
    await asyncio.gather(coroutine_1(), coroutine_2())

if __name__ == "__main__":
    sync_main()

    asyncio.run(async_main())