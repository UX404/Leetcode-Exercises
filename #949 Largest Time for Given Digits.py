'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9
'''


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        l1, l2, l3 = [], [], []  # 0-2/3-5/6-9
        result = ""

        for i in A:
            if i <= 2:
                l1.append(i)
            elif i <= 5:
                l2.append(i)
            else:
                l3.append(i)
        l1.sort()
        l2.sort()
        l3.sort()

        # 1
        if len(l1) == 2 and not l2 and l1[-1] == 2:  # 2,0,6,6
            result += str(l1.pop(0))
        elif l1:
            result += str(l1.pop())
        else:
            return ""

        # 2
        if result == '2':
            if l2 and l2[0] == 3:
                result += str(l2.pop(0))
            elif l1:
                result += str(l1.pop())
            else:
                return ""
        else:
            if l3:
                result += str(l3.pop())
            elif l2:
                result += str(l2.pop())
            elif l1:
                result += str(l1.pop())
            else:
                return ""

        # :
        result += ':'

        # 3
        if l2:
            result += str(l2.pop())
        elif l1:
            result += str(l1.pop())
        else:
            return ""

        # 4
        if l3:
            result += str(l3.pop())
        elif l2:
            result += str(l2.pop())
        elif l1:
            result += str(l1.pop())
        else:
            return ""

        return result