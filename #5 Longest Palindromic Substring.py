'''
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''


# Comparing from the center
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for n in range(len(s)):
            p, q = n, n + 1
            if p >= 0 and q < len(s) and s[p] == s[q]:
                while p >= 0 and q < len(s) and s[p] == s[q]:
                    p -= 1
                    q += 1
                if q - p > len(ans):
                    ans = s[p + 1:q]
            p, q = n, n + 2
            if p >= 0 and q < len(s) and s[p] == s[q]:
                while p >= 0 and q < len(s) and s[p] == s[q]:
                    p -= 1
                    q += 1
                if q - p > len(ans):
                    ans = s[p + 1:q]
        return ans