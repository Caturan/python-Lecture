"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
"""
import time
nums = [1,12,-5,-6,50,3]
k = 4
lenn = len(nums)
print(lenn)

start = nums[0]
end = nums[lenn-k]
print(start)
print(end)

lop = lenn - (k-1)
print(lop)

result = []
count = 0
print("------------------")

u = 0

while count <= lop-1:
    temp = nums[u]
    for i in range(k-1):
        temp += nums[u+i+1]   
        print(temp)
        
    sum = temp / k 
    result.append(sum)
    print(sum)
    count += 1
    u += 1

print(max(result))
    
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum    
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
"""