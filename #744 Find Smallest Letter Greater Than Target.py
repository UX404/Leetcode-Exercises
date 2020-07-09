'''
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
'''


# 1 Sort(), o(nlogn)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        letters.sort(reverse=True)
        index = letters.index(target)
        return letters[(index-1) % len(letters)]


# 2 Hash, o(n)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        loc = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        distance = []
        for i in letters:
            distance.append((loc[i] - loc[target] - 1) % 26)
        min_distance = distance.index(min(distance))
        return letters[min_distance]


# 3 Order search, o(n)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = 0
        while target >= letters[n]:
            n += 1
            if n == len(letters):
                return letters[0]
        return letters[n]


# 4 Binary search, o(logn)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target)
        lh, rh = 0, len(letters)-1
        while lh < rh:
            mid = (lh + rh ) // 2
            if target >= letters[mid]:
                lh = mid + 1
            else:
                rh = mid
        if letters[lh] == target:
            return letters[0]
        else:
            return letters[lh]