'''
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
'''


# 1 Max three times
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = nums[0]
        for i in nums:
            if i > first: first = i
        n = 0
        while n < len(nums):
            if nums[n] == first: nums.pop(n)
            else: n += 1
        if nums: second = nums[0]
        else: return first
        for i in nums:
            if i > second: second = i
        n = 0
        while n < len(nums):
            if nums[n] == second: nums.pop(n)
            else: n += 1
        if nums: third = nums[0]
        else: return first
        for i in nums:
            if i > third: third = i
        return third


# 2 Sort
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3: return nums[-1]
        else: return nums[-3]