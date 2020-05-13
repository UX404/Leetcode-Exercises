'''

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        for n in range(len(nums)):
            nums[n] = [n, nums[n]]
        nums.sort(key=lambda x:x[1], reverse=True)
        nums[0][1] = "Gold Medal"
        if len(nums) > 1:
            nums[1][1] = "Silver Medal"
            if len(nums) > 2:
                nums[2][1] = "Bronze Medal"
        for n in range(3, len(nums)):
            nums[n][1] = str(n+1)
        result = [0 for n in range(len(nums))]
        for i in nums:
            result[i[0]] = i[1]
        return result