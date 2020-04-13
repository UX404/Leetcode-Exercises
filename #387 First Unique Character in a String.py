'''

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''


# 1 Basic method
class Solution:
    def firstUniqChar(self, s: str) -> int:
        loc = {}
        for n in range(len(s)): loc[s[n]] = n
        s = list(s)
        n = 0
        while n < len(s):
            repeat = False
            m = n+1
            while m < len(s):
                if s[n] == s[m]:
                    print(s[n], s[m])
                    s.pop(m)
                    repeat = True
                else: m += 1
            if not repeat: return loc[s[n]]
            n += 1
        return -1


# 2 Hash
class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat = {}
        for i in s:
            if repeat.__contains__(i): repeat[i] += 1
            else: repeat[i] = 1
        for n in range(len(s)):
            if repeat[s[n]] == 1: return n
        return -1