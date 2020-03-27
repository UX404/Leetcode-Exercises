'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''


# 1 Sort()
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for n in range(len(nums)):
            if nums[n] != n: return n
        return len(nums)


# 2 Hash
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exist = {}
        for i in nums:
            exist[i] = None
        for n in range(len(nums) + 1):
            if not exist.__contains__(n): return n