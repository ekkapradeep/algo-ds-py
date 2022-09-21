"""
https://leetcode.com/problems/search-insert-position

35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4


"""

def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    mid = 1
    while left <= right:
        mid = left + ((right-left)//2)
        
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return left


nums = [1,3,5,6]
target = 2
print(search_insert(nums,target))

nums = [1,3,5,6]
target = 5
print(search_insert(nums,target))

nums = [1,3,5,6]
target = 7
print(search_insert(nums,target))
