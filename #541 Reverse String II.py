'''
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
'''


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p = 1
        result = ""
        while (p-1)*k <= len(s):
            result += s[(p-1)*k: p*k][::-1]
            result += s[p*k: (p+1)*k]
            p += 2
        return result
