'''

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        left = []
        temp = len(S)
        for i in S:
            if i == C: temp = 0
            else: temp += 1
            left.append(temp)
        right = []
        temp = len(S)
        for i in S[::-1]:
            if i == C: temp = 0
            else: temp += 1
            right.append(temp)
        return [min(left[n], right[len(right)-1-n]) for n in range(len(left))]