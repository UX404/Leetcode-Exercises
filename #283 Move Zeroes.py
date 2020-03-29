'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''


# 1 Create a supplementary list
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        moved = [i for i in nums if i != 0]
        for n in range(len(moved)):
            nums[n] = moved[n]
        for n in range(len(moved), len(nums)):
            nums[n] = 0

# 2 Exchange in place
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                if n != index:
                    nums[index] = nums[n]
                    nums[n] = 0
                index += 1