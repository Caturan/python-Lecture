import threading
"""
    A race condition is a type of concurrency issue that occurs when two or more processes or threads access shared data and try to change it at the same time.
    The outcome of the process or threads is dependent on the sequence of the processes or threads is dependent on the sequence or timing of their execution. 
    To simulate the problem and understand the solution, we will use a simple counter. 
"""
class Counter:
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1
# To use this simple class, we will create a thread. 
class IncreaseCounter(threading.Thread):
    def __init__(self, counter, n):
        super().__init__()
        self.counter = counter
        self.n = n

    def run(self):
        for _ in range(self.n):
            self.counter.increase()
# Now let's craete a function to create m number of threads, which increases the counter n times:
def main(n: int, m: int):
    counter = Counter()
    threads = []
    for _ in range(m):
        t = IncreaseCounter(counter, n)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Expected: {n*m}, Actual: {counter.count}")
    return counter.count
# Nothing seems problematic in this simple implementation, but let's test this program with different sizes: 
number_of_threads = 4
for size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    try:
        assert main(size, number_of_threads) == size * number_of_threads
    except AssertionError:
        print(f"Failed for size {size}")
    else:
        print(f"Success for size {size}")

"""
    When we run this code, it is highly possible that the test fails with large sizes. It is because that increasing the value of an integer is not a one single piece job. 
    To increase a value, we should roughly complete the following steps:
        - Read the current value
        - Increase the value
        - Write the new value
    Therefore with multi threads, even with the global interpreter lock, sometimes these steps can interfere each other and lead to inconsistent results. 
    The simplest solution is to use locks to control the access to a particular variable. Let's modify our Counter class:
"""
class LockedCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increase(self):
        with self.lock:
            self.count += 1
    
# To use this simple class, we will create a thread. 
class IncreaseCounter(threading.Thread):
    def __init__(self, counter, n):
        super().__init__()
        self.counter = counter
        self.n = n

    def run(self):
        for _ in range(self.n):
            self.counter.increase()
# Now let's craete a function to create m number of threads, which increases the counter n times:
def main(n: int, m: int):
    counter = LockedCounter()
    threads = []
    for _ in range(m):
        t = IncreaseCounter(counter, n)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"Expected: {n*m}, Actual: {counter.count}")
    return counter.count
# Nothing seems problematic in this simple implementation, but let's test this program with different sizes: 
number_of_threads = 4
for size in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    try:
        assert main(size, number_of_threads) == size * number_of_threads
    except AssertionError:
        print(f"Failed for size {size}")
    else:
        print(f"Success for size {size}")

"""
    If we start to use this class intead of the previous one, now our variable is thread safe with the help of the lock.
    Howewer this lock also introduces a new performance bottleneck to our solution. 
"""