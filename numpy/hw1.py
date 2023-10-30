"""
replace_center_with_minus_one(d, n, m) 
This function created as n-by-n numpy array populated with random integers that have up to d digits. 
 It then replaces the central m-by-m part of this array with -1. 

Parameters: 
    * d: Number of digits for the random integers. 
    * n: Size of the main array. 
    * m: Size of the central array that will be replaced with -1. 

Returns:
    * A modified numpy array with its center replaced with -1. 

Exceptions:
    * ValueError: This exception is raised in the following scenerios:
        * If m > n
        * If d <= 0
        * If n < 0 
        * If m < 0
"""

import numpy as np 

def replace_center_with_minus_one(d, n, m):
    if m > n or d <= 0 or n < 0 or m < 0:
        raise ValueError("Error the input parameter")

    random_array = np.random.randint(10 ** (d-1), 10 ** d, size=(n, n))

    start_indx = (n- m) // 2
    end_indx = start_indx + m 

    random_array[start_indx:end_indx, start_indx:end_indx] = -1

    return random_array

def main():
    print("Hello")
    if "random" in dir(np):
      print("Y")
    else:
     print("N")

    result = replace_center_with_minus_one(3, 5, 3)
    print(result)
    
if __name__ == "__main__":
    main()