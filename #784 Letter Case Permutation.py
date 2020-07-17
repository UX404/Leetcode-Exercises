'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        temp1 = [S]
        result = []
        for n in range(len(S)):
            if S[n].isalpha:
                temp2 = []
                for i in temp1:
                    temp2.append(i[:n] + i[n].upper() + i[n+1:])
                    temp2.append(i[:n] + i[n].lower() + i[n+1:])
                temp1 = temp2
                result += temp1
        return list(set(result))
