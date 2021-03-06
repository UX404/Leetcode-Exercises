'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''


# 1 Basic method
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextnum = {}
        for n in range(len(nums2)):
            found = False
            for i in nums2[n + 1:]:
                if i > nums2[n]:
                    nextnum[nums2[n]] = i
                    found = True
                    break
            if not found: nextnum[nums2[n]] = -1

        for n in range(len(nums1)):
            nums1[n] = nextnum[nums1[n]]
        return nums1


# 2 Stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextnum = {}
        stack = []
        pointer = 0
        while pointer < len(nums2):
            if not stack or nums2[pointer] < stack[-1]:
                stack.append(nums2[pointer])
                pointer += 1
            elif nums2[pointer] > stack[-1]:
                nextnum[stack.pop()] = nums2[pointer]
        while stack:
            nextnum[stack.pop()] = -1

        for n in range(len(nums1)):
            nums1[n] = nextnum[nums1[n]]
        return nums1