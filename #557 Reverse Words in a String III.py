'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''


# 1 Basic method
# This method is suitable for strings like "   Let's   take LeetCode    contest   "
class Solution:
    def reverseWords(self, s: str) -> str:
        s += ' $ '  # solve the problem that p<len(s) is judged every time
        p = 0
        result = ""
        while p != len(s) - 1:
            while s[p] == ' ':
                p += 1
            sub = ""
            while s[p] != ' ':
                sub = s[p] + sub
                p += 1
            result += sub + ' '
        return result[:-3]


# 2 Split()
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        s = s.split()
        for i in s:
            result += i[::-1] + ' '
        return result[:-1]