"""
https://leetcode.com/problems/first-bad-version

278. First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1

"""
BAD_VERSION = 7

def is_bad_version(n):
    return n >= BAD_VERSION

def first_bad_version(n):
    first_version = 1
    last_version = n
    min_bad_version = n

    while first_version <= last_version:
        mid_version = first_version + ((last_version - first_version) // 2)
        if is_bad_version(mid_version) == True:
            min_bad_version = min(min_bad_version, mid_version)
            last_version = mid_version - 1
        else:
            first_version = mid_version + 1
    
    return min_bad_version

print(first_bad_version(10))