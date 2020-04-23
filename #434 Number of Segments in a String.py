'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''


# 1 Split
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

# 2 Basic method
class Solution:
    def countSegments(self, s: str) -> int:
        s = ' ' + s + ' '
        n = 0
        count = 0
        while True:
            while s[n] == ' ':
                n += 1
                if n == len(s): return count
            while s[n] != ' ': n += 1
            count += 1