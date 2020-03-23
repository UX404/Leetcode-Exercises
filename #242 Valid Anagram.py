'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = {}
        for i in s:
            if dictionary.__contains__(i): dictionary[i] += 1
            else: dictionary[i] = 1
        for i in t:
            if dictionary.__contains__(i): dictionary[i] -= 1
            else: return False
        for i in dictionary.values():
            if i != 0: return False
        return True