'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        error = sum(nums[:3]) - target
        for n in range(len(nums)):
            target2 = target - nums[n]
            # print(target, nums[n], target2)
            nums2 = nums[:n] + nums[n+1:]
            p, q = 0, 1
            error2 = nums2[p] + nums2[q] - target2
            for r in range(2, len(nums2)):
                delta1 = abs(error2)
                delta2 = abs(nums2[r] + nums2[q] - target2)
                delta3 = abs(nums2[p] + nums2[r] - target2)
                # print(n, p, q, r, delta1, delta2, delta3, error2)
                if delta2 <= delta3 and delta2 < delta1:
                    error2 = nums2[r] + nums2[q] - target2
                    p = q
                    q = r
                elif delta3 < delta2 and delta3 < delta1:
                    error2 = nums2[p] + nums2[r] - target2
                    q = r
            if abs(error2) < abs(error):
                error = error2
        return error + target