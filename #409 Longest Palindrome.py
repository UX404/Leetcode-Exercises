'''

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''


# 1 Collections
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        single = False
        count = Counter(s)
        for i in count.keys():
            if count[i] % 2 == 0:
                length += count[i]
            else:
                length += count[i] - 1
                single = True
        return length + int(single)


# 2 Basic method
class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        count = {}
        for i in s:
            if count.__contains__(i):
                count[i] += 1
                if count[i] % 2 == 0: length += 2
            else: count[i] = 1
        for j in count.values():
            if j % 2 == 1: return length + 1
        return length