"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

1491. Average Salary Excluding the Minimum and Maximum Salary

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
"""

from typing import List


def average_salary(salaries: List[int]) -> float:
    min_sal = float("inf")
    max_sal = float("-inf")
    total_sal = 0
    for sal in salaries:
        min_sal = min(min_sal, sal)
        max_sal = max(max_sal, sal)
        total_sal += sal
    
    ave_sal = (total_sal - min_sal - max_sal)/ (len(salaries) - 2)
    return ave_sal

salary = [4000,3000,1000,2000]
print(average_salary(salary))
salary = [1000,2000,3000]
print(average_salary(salary))