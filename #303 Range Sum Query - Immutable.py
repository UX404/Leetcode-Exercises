'''
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''


# 1 Basic method (1212ms)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i: j+1])


# 2 One buffer (452ms)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.buffer = sum(nums)
        self.lh = 0
        self.rh = len(nums) - 1

    def sumRange(self, i: int, j: int) -> int:
        if i < self.lh: self.buffer += sum(self.nums[i: self.lh])
        else: self.buffer -= sum(self.nums[self.lh: i])
        if j > self.rh: self.buffer += sum(self.nums[self.rh+1: j+1])
        else: self.buffer -= sum(self.nums[j+1: self.rh+1])
        self.lh = i
        self.rh = j
        return self.buffer


# 3 All buffer (TLE)
class NumArray:

    def __init__(self, nums: List[int]):
        self.buffer = {}

        for n in range(len(nums)):
            self.buffer[n] = dict()
            for m in range(n, len(nums)):
                self.buffer[n][m] = sum(nums[n: m+1])

    def sumRange(self, i: int, j: int) -> int:
        return self.buffer[i][j]


# 4 Former buffer (76ms)
class NumArray:

    def __init__(self, nums: List[int]):
        self.buffer = {}

        accumulator = 0
        self.buffer[-1] = accumulator
        for n in range(len(nums)):
            accumulator += nums[n]
            self.buffer[n] = accumulator

    def sumRange(self, i: int, j: int) -> int:
        return self.buffer[j] - self.buffer[i - 1]