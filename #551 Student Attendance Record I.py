'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''


class Solution:
    def checkRecord(self, s: str) -> bool:
        s += "PP"
        A_count = 0
        L_count = 0
        for i in s:
            if i == 'A':
                A_count += 1
                if A_count == 2: return False
            elif i == 'L':
                L_count += 1
                if L_count == 3: return False
                continue
            L_count = 0
        return True