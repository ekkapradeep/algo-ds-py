"""
https://leetcode.com/problems/running-sum-of-1d-array/

1480. Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

"""

from typing import List


def runningSum(nums: List[int]) -> List[int]:
    result = []
    running_sum = 0
    
    for n in nums:
        running_sum += n
        result.append(running_sum)
    return result


nums = [1,1,1,1,1]
print(nums)
print(runningSum(nums))