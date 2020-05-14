'''
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
'''


# 1 o(n/2)
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        spd = 0
        for n in range(num//2, 0, -1):
            if num//n == num/n:
                spd += n
                if spd > num: return False
        if spd == num: return True


# 2 o(sqrt(n))
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1: return False
        spd = 1
        for n in range(2, int(num**0.5)+1):
            if num//n == num/n:
                spd += n
                spd += num//n
                if spd > num: return False
        if spd == num: return True