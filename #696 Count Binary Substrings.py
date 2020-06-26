'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        n1, n2 = 0, 0
        for n in range(1, len(s)):
            if s[n] != s[n1]:
                n2 = n
                break
        if n2 == 0: return 0
        for n in range(n2+1, len(s)):
            if s[n] != s[n2]:
                result += min(n - n2, n2 - n1)
                n1 = n2
                n2 = n
        result += min(len(s) - n2, n2 - n1)
        return result