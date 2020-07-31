'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        for i in S:
            if i == '#':
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)
        stack2 = []
        for i in T:
            if i == '#':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        return stack1 == stack2