"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:

    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1

"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num  
            elif num <= second:
                second = num  
            else:
                return True
        return False


"""
What is the 'inf':
float('inf') is a way to represent positive infinity in Python. It is useful when you need a value that is guaranteed to be larger than any other number, which can be helpful for comparison purposes.

How It Works:
- Positive Infinity: float('inf') represents a number that is larger than any other finite number.
- Negative Infinity: Similarly, float('-inf') represents a number that is smaller than any other finite number.

In the Context of the Problem:
In the increasingTriplet function, float('inf') is used to initialize first and second to very large values so that any number in the list will be smaller and can replace them. 
This helps in tracking the smallest and the second smallest numbers to find an increasing triplet in the list.
"""