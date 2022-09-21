"""
https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9

"""

def count_odds(low:int, high:int):
    odd_count = 0
    if low % 2 != 0:
        odd_count +=1
        low = low +1
    if high % 2 != 0:
        odd_count +=1
        high -= 1
    inrange_count = (high - low) // 2
    odd_count += inrange_count
    return odd_count

print(count_odds(1,13))

