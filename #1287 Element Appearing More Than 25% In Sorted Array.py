'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.



Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6


Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
'''


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        threshold = len(arr) / 4
        compare = arr[0]
        count = 0
        for i in arr:
            if i == compare:
                count += 1
                if count > threshold:
                    return i
            else:
                compare = i
                count = 1