'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6


Example 2:

Input: [1,2,3,4]
Output: 24


Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        min1, min2 = 0, 0
        for i in nums:
            min1 = min(min1, i)
        for n in range(len(nums)):
            if min1 == nums[n]:
                nums.pop(n)
                break
        for i in nums:
            min2 = min(min2, i)
        for n in range(len(nums)):
            if min2 == nums[n]:
                nums.pop(n)
                break
        max1, max2, max3 = min1, min1, min1
        for i in nums2:
            max1 = max(max1, i)
        nums2.remove(max1)
        for i in nums2:
            max2 = max(max2, i)
        nums2.remove(max2)
        for i in nums2:
            max3 = max(max3, i)
        nums2.remove(max3)
        return max(max1*max2*max3, min1*min2*max1)


# min/max method
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums2 = nums.copy()
        min1 = min(0, min(nums))
        if min1 != 0:
            nums.remove(min1)
            min2 = min(0, min(nums))
        else:
            min2 = 0
        max1 = max(nums2)
        nums2.remove(max1)
        max2 = max(nums2)
        nums2.remove(max2)
        max3 = max(nums2)
        return max(max1*max2*max3, min1*min2*max1)

# This sucks.
