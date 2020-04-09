'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lh, rh = 0, num + 1
        while lh < rh:
            mid = int((lh + rh) / 2)
            if mid * mid < num: lh = mid + 1
            elif mid * mid > num: rh = mid
            else: return True
        return False