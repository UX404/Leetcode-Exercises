'''

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a': None, 'e': None, 'i': None, 'o': None, 'u': None, 'A': None, 'E': None, 'I': None, 'O': None, 'U': None}
        s = list(s)
        lh = 0
        rh = len(s) - 1
        while lh < rh:
            while not vowels.__contains__(s[lh]) and lh < rh: lh += 1
            while not vowels.__contains__(s[rh]) and lh < rh: rh -= 1
            if lh < rh:
                temp = s[lh]
                s[lh] = s[rh]
                s[rh] = temp
            lh += 1
            rh -= 1
        result = ""
        for i in s: result += i
        return result