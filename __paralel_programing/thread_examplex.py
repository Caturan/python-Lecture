import threading

"""
    Q1: Write a Python program to create multiple threads and print their names. 
"""
def print_thread_names():
    print("Current thread name:", threading.current_thread().name)

threads = []
for i in range(7):
    thread = threading.Thread(target=print_thread_names)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


"""
    Q2: Write a Python program that creates two threads to find and print even and odd numbers from 30 to 50. 
"""

import time
def print_even_numbers():
    print("List of even numbers:")
    for i in range(30, 51, 2):
        print(i, end = " ")
        time.sleep(1)


def print_odd_numbers():
    print("\nList of odd numbers:")
    for i in range(31, 51, 2):
        print(i, end = " ")
        time.sleep(1)

even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

even_thread.start()
even_thread.join()

odd_thread.start()
odd_thread.join()