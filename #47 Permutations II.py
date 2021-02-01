'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def search(begin, nums):
            if begin == len(nums) and all(nums != i for i in ans):
                ans.append(nums)
            for n in range(begin, len(nums)):
                nums_temp = nums.copy()
                nums_temp[begin], nums_temp[n] = nums_temp[n], nums_temp[begin]
                search(begin+1, nums_temp)
        
        search(0, nums)
        return ans