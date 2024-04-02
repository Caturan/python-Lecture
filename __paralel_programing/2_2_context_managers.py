    #  Context Managers
"""
    One another key point, which is very commonly used in asynchronous programs, is the asynchronous context managers. 
    Let' take a detailed investiogation of this design pattern. 

    Context manager is an object designed to manage the setup and teardown of a resource. It is used to ensure that resources, such as files or network connections, 
    are efficiently used and properly closed after their operations completed. 
    To define a context manager from a class, we should define the magic methods __enter__ and __exit__.
"""
    # Synchronous Context Manager
"""
    __enter__ : What to do when entering the context
    __exit__: What to do when exiting the context
"""

class ContextManager:
    def __init__(self) -> None:
        print(f"Initializing {self.__class__.__name__}")

    def __enter__(self) -> "ContextManager":
        print(f"Entering {self.__class__.__name__}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(f"Exiting {self.__class__.__name__}")
        print(f"e: {exc_type}, v: {exc_val}, tb: {exc_tb}")
        return True

    def __call__(self, task: str) -> None:
        print(f"Calling {task}")
        return None

def main() -> None:
    with ContextManager() as cm:
        cm("example task")
    print()
    contextobject = ContextManager()
    contextobject("obje")

if __name__ == "__main__":
    main()

print()

    # Asynchronous Context Manager
"""
    __aenter__: What to do when entering the context
    __aexit__: What to do when exiting the context
 """
import asyncio

class AsyncContextManager:
    def __init__(self) -> None:
        print(f"Initializing {self.__class__.__name__}")

    async def __aenter__(self) -> "AsyncContextManager":
        print(f"Entering {self.__class__.__name__}")
        await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(f"Exiting {self.__class__.__name__}")
        print(f"e: {exc_type}, v: {exc_val}, tb: {exc_tb}")
        await asyncio.sleep(1)
        return True

    async def __call__(self, task: str) -> None:
        print(f"Calling {task}")
        await asyncio.sleep(1)
        return None

async def async_main() -> None:
    async with AsyncContextManager() as acm:
        await acm("example task")
    print()
    asyncobje = AsyncContextManager()
    await asyncobje("async_obje")

if __name__ == "__main__":
    asyncio.run(async_main())