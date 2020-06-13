'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
'''


# 1 o(n^2), Basic method
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = []
        for n in range(1, len(nums)+1):
            if nums.count(n) == 2:
                result.append(n)
                break
        for n in range(1, len(nums)+1):
            if nums.count(n) == 0:
                result.append(n)
                break
        return result


# 2 o(n^2), Quick sort
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        nums.sort()
        for n in range(1, len(nums)):
            if nums[n] == nums[n-1]:
                result[0] = nums[n]
            elif nums[n] == nums[n-1] + 2:
                result[1] = nums[n] - 1
        if nums[0] != 1: result[1] = 1
        elif nums[-1] != len(nums): result[1] = len(nums)
        return result


# 3 o(n), Hash
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        compare = dict.fromkeys(range(1, len(nums)+1))
        for i in nums:
            if compare.__contains__(i):
                del compare[i]
            else:
                result[0] = i
        result[1] = list(compare.keys())[0]
        return result