'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
'''


# 1 Basic method
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B: return True
        for n in range(len(A)):
            if A[n] == B[0]:
                if A[n:] + A[:n] == B:
                    return True
        return False


# 2 Substring
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and A in B*2