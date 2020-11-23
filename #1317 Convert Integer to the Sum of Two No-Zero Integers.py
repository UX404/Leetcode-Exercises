'''
Given an integer n. No-Zero integer is a positive integer which doesn't contain any 0 in its decimal representation.

Return a list of two integers [A, B] where:

A and B are No-Zero integers.
A + B = n
It's guarateed that there is at least one valid solution. If there are many valid solutions you can return any of them.



Example 1:

Input: n = 2
Output: [1,1]
Explanation: A = 1, B = 1. A + B = n and both A and B don't contain any 0 in their decimal representation.
Example 2:

Input: n = 11
Output: [2,9]
Example 3:

Input: n = 10000
Output: [1,9999]
Example 4:

Input: n = 69
Output: [1,68]
Example 5:

Input: n = 1010
Output: [11,999]


Constraints:

2 <= n <= 10^4
'''


# 1 For
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for m in range(1, n):
            if (not '0' in str(m)) and (not '0' in str(n-m)):
                return [m, n-m]


# 2 Scan from right to left
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        A = n
        base = 1
        while A // base >= 10:
            bit = (A // base) % 10
            if bit == 9:
                A -= 2 * base
            else:
                A -= (bit + 1) * base
            base *= 10
        if A == n:
            return [1, n-1]
        else:
            return [A, n-A]