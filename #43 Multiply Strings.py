'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans_int = [0] * (len(num1) + len(num2))
        ans_str = ""
        
        # multiply by bit
        for n1, s1 in enumerate(num1):
            for n2, s2 in enumerate(num2):
                subans = int(s1) * int(s2)
                ans_int[n1+n2] += (subans % 10)
                ans_int[n1+n2+1] += (subans // 10)
        
        # address carry
        for n in range(len(ans_int)-1):
            ans_int[n+1] += (ans_int[n] // 10)
            ans_int[n] = (ans_int[n] % 10)
        
        # convert to string
        p = len(ans_int) - 1
        while p >= 0 and ans_int[p] == 0:
            p -= 1
        while p >= 0:
            ans_str += str(ans_int[p])
            p -= 1
        if ans_str == "":
            ans_str += '0'
        return ans_str