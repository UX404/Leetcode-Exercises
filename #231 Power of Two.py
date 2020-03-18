'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''


# 1 Basic method
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 1:
            if n == 1: return True
            n = n / 2
        return False


# 2 bit -> dec
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bit = '1'
        while n >= int(bit, 2):
            if n == int(bit, 2): return True
            bit += '0'
        return False


# 3 Recursion
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        elif n == 1: return True
        elif n != int(n): return False
        else: return self.isPowerOfTwo(n / 2)