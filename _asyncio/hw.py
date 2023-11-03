import asyncio
import time

"""
def decarator2(fn):
    async def _await():
        print("Cat")
        fn()
        await time.sleep(2)
        print("TURAN")  
    return _await()
"""
"""
def func1():
    print("Hello")

def func2():
    print("CAT")

func1()
func2()
"""
"""
async def decator3():
    def cour1():
        print("1 work")
        await asyncio.sleep(3)
        print("1 ENd")
    return cour1()

asyncio.run(decator3())
"""
"""
def decarator(fn):
    def wrapper():
        print("D1 work")
        fn()
        print("D1 end")
    return wrapper
""

"""
"""
@decarator2
def say():
    print("hellLLO")

asyncio.run(say())
"""

def awaitme(func):
    async def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if asyncio.iscoroutinefunction(func):
            return await result
        return result

    return wrapper


# Example usage:

@awaitme
def regular_function(x, y):
    return x + y

async def coroutine_function(x, y):
    await asyncio.sleep(1)
    return x + y

# Using the decorator with both regular and coroutine functions
result1 = regular_function(3, 4)
result2 = coroutine_function(3, 4)

print(result1)  # Output: 7
print(result2)  # Output: 7
