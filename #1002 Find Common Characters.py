'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.



Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        for n in range(len(A)):
            A[n] = Counter(A[n])
        common = A[0]
        for count in A[1:]:
            for item in common.items():
                if count.__contains__(item[0]):
                    common[item[0]] = min(count[item[0]], item[1])
                else:
                    common[item[0]] = 0
        result = []
        for item in common.items():
            result += item[1] * [item[0]]
        return result


# Simplified
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        for n in range(len(A)):
            A[n] = Counter(A[n])
        common = A[0]
        for count in A[1:]:

            common &= count  # Use '&' to merge Counters

        result = []
        for item in common.items():
            result += item[1] * [item[0]]
        return result