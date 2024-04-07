
"""
    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up. 

    Given list is . The maximum score is [2,3,6,6,5], second maximum is 5. Hence, we print as the runner-up score. 
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    
    arr = sorted(set(arr), reverse=True)
    
    print(arr[1])
