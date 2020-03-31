'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str += ' '
        compare1 = ""
        compare2 = ""
        dictionary = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        pointer = 0

        for i in pattern:
            if dictionary.__contains__(i):
                compare1 += dictionary[i]
            else:
                dictionary[i] = alphabet[pointer]
                compare1 += alphabet[pointer]
                pointer += 1

        dictionary = {}
        pointer = 0
        lh = 0
        rh = 0
        while lh < len(str):
            rh += 1
            if str[rh] == ' ':
                if dictionary.__contains__(str[lh: rh]):
                    compare2 += dictionary[str[lh: rh]]
                else:
                    dictionary[str[lh: rh]] = alphabet[pointer]
                    compare2 += alphabet[pointer]
                    pointer += 1
                lh = rh + 1
                rh = lh
        if compare1 == compare2:
            return True
        else:
            return False