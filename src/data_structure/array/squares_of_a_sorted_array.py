"""
https://leetcode.com/problems/squares-of-a-sorted-array

977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


"""


def sorted_squares(nums):
    result = [-1] * len(nums)
    left,right, current = 0, len(nums) - 1, len(nums) -1
    
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[current] = nums[left] **2
            left +=1
        else:
            result[current] = nums[right] **2
            right -=1
        current -=1
    
    return result



nums = [-4,-1,0,3,10]
print(nums)
print(sorted_squares(nums))

nums = [-7,-3,2,3,11]
print(nums)
print(sorted_squares(nums))