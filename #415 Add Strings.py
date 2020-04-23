'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        redigit = "0123456789"
        if len(num1) > len(num2):
            num2 = (len(num1) - len(num2) + 1) * '0' + num2
            num1 = '0' + num1
        else:
            num1 = (len(num2) - len(num1) + 1) * '0' + num1
            num2 = '0' + num2
        c = 0
        result = ""
        for n in range(len(num1)-1, -1, -1):
            s = (digit[num1[n]] + digit[num2[n]] + c) % 10
            result += redigit[s]
            c = (digit[num1[n]] + digit[num2[n]] + c) // 10
        if result[-1] == '0': return result[-2::-1]
        else: return result[::-1]