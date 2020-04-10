'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''


class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = a % 0x10000
        b = b % 0x10000
        while b:
            a0 = a
            a = a0 ^ b
            b = (a0 & b) << 1
        a = a % 0x10000
        if a < 0x8000: return a
        else: return ~(a ^ 0xFFFF)