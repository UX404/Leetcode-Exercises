'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:

Input: 3
Output: False
'''


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0, int(sqrt(c/2)) + 1):
            b = sqrt(c - a*a)
            if b == int(b):
                return True
        return False