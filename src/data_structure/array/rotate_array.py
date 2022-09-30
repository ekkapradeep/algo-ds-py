"""
https://leetcode.com/problems/rotate-array/

189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

"""

from typing import List

#time complexity: O(n)
#space complexity: O(n)

def rotate_array1(nums: List[int], k: int) -> None:
    result = []
    k = k % len(nums)
    print(k)
    for i in range(k, len(nums)):
        result.append(nums[i])
    for i in range(k):
        result.append(nums[i])
    for i,n in enumerate(result):
        nums[i] = n

def rotate_array2(nums: List[int], k: int) -> None:
    def reverse(start, end):
        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start+=1
            end-=1
    reverse(0,len(nums)-1)
    reverse(0,len(nums)-k-1)
    reverse(len(nums)-k,len(nums)-1)


nums = [-1,-100,3,99]
k = 202
#Output: [3,99,-1,-100]
print(nums)
rotate_array1(nums,k)
print(nums)

nums = [-1,-100,3,99]
k = 202
#Output: [3,99,-1,-100]
print(nums)
rotate_array2(nums,k)
print(nums)

"""
1,2,3,4,5 -> 1 => 2,3,4,5,1
5,4,3,2,1
2,3,4,5,1

1,2,3,4,5 ->2 => 3,4,5,1,2
5,4,3,2,1

"""
