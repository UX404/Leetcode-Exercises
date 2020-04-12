'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''


# 1 Hash
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        compare = {}
        for i in magazine:
            if compare.__contains__(i): compare[i] += 1
            else: compare[i] = 1
        for j in ransomNote:
            if compare.__contains__(j):
                if compare[j] == 0: return False
                compare[j] -= 1
            else: return False
        return True


# 2 Collections
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if Counter(ransomNote) - Counter(magazine): return False
        else: return True

'''
>>> a = collections.Counter('abbab')
Counter({'b': 3, 'a': 2})
>>> b = collections.Counter('bbabb')
Counter({'b': 4, 'a': 1})
>>> a-b
Counter({'a': 1})
'''