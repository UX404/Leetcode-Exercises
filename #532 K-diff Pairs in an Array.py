'''
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
'''


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        p1, p2 = 0, 1
        count = 0
        while p2 < len(nums):
            if nums[p1] + k < nums[p2]:
                p1 += 1
                if p1 == p2: p2 += 1
            elif nums[p1] + k > nums[p2]:
                p2 += 1
            else:
                count += 1
                while p2+1 < len(nums) and nums[p2] == nums[p2+1]:
                    p2 += 1
                p2 += 1
        return count