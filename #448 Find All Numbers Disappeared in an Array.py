'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        exclude = dict.fromkeys(range(1, len(nums) + 1))
        for i in nums:
            if exclude.__contains__(i): del exclude[i]
            else: continue
        return [i for i in exclude]