'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def compare(lh, rh):
            while lh < rh:
                if s[lh] != s[rh]:
                    return False
                lh += 1
                rh -= 1
            return True

        lh, rh = 0, len(s) - 1
        while lh < rh:
            if s[lh] != s[rh]:
                return compare(lh + 1, rh) or compare(lh, rh - 1)
            lh += 1
            rh -= 1
        return True