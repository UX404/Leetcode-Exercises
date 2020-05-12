'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"
        isNegative = False
        result = ""
        if num < 0:
            isNegative = True
            num = -num
        while num != 0:
            result += str(num % 7)
            num //= 7
        if isNegative:
            return '-' + result[::-1]
        else:
            return result[::-1]