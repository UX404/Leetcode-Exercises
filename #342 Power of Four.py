'''

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
'''


# 1 Basic Method
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        while num == int(num):
            if num == 1: return True
            num /= 4
        return False


# 2 Base 2
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        num = num ** 0.5
        if num != int(num): return False
        num = bin(int(num))
        if num[2] != '1': return False
        for i in num[3:]:
            if i != '0': return False
        return True