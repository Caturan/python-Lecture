
"""
    These articles discusses the concept data sharing and message passing between processes while using multiprocessing module in Python. 
    In multiprocessing, any newly created process will do following:
    - run independently
    - have their own memory space
"""

import multiprocessing

result = [] # empty list with global scope

def square_list(mylist):
    global result
    for num in mylist:
        result.append(num * num)
    print("Result(in process p1): {}".format(result))

if __name__ == "__main__":
    mylist = [1,2,3,4]

    p1 = multiprocessing.Process(target=square_list, args=(mylist,))

    p1.start()
    p1.join()

    print("Result(in main program): {}".format(result))
"""
    In above example, we try to print contents of global list result at two places:
    - In square_list function. Since, this function is called by process p1, result list is changed in memory space of process p1 only. 
    - After the completion of process p1 in main program. Since main program is run by a different process, its memory space still contains the empty result list. 
"""

"""
Shared Memory:
    Multiprocessing module provides Array and Value objects to share data between processes. 
    - Array: a ctypes array allocated from shared memory
    - Value: a ctypes object allocated from shared memory
"""
# Example above use Array and Value for sharing data processes:
import multiprocessing

def square_list(mylist, result, square_sum):
    for i, num in enumerate(mylist):
        result[i] = num * num 

    square_sum.value = sum(result)

    print("Result(in process p1): {}".format(result[:]))
    print("Sum of squares(in process p1): {}".format(square_sum.value))

if __name__ == "__main__":
 
    mylist = [1,2,3,4]
    result = multiprocessing.Array('i',4) # First argument is the data type. 'i' stands for whereas 'd' stands for float data type. Second argument is the size of array. 
    square_sum = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

    p1.start()
    p1.join()

    print("Result(in main program): {}".format(result[:]))  # We use result[:] to print complete array. 
    print("Sum of squares(in main program): {}".format(square_sum.value))

