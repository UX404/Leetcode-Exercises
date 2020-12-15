'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


# Double pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for n in range(len(nums)):
            nums_2 = nums[:n] + nums[n+1:]
            lh, rh = 0, len(nums_2)-1
            while lh < rh:
                # print(n, nums_2, lh, rh)
                if nums_2[lh] + nums_2[rh] + nums[n] < 0:
                    lh += 1
                elif nums_2[lh] + nums_2[rh] + nums[n] > 0:
                    rh -= 1
                else:
                    triplet = [nums_2[lh], nums[n], nums_2[rh]]
                    triplet.sort()
                    if not triplet in ans:
                        ans.append(triplet)
                    lh += 1
                    rh -= 1
        return ans