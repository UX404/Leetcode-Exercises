'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''


# 1 Basic method
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort = nums.sort()
        count = 0
        for n in range(len(nums))
            if nums[n] == sort[n]:
                count += 1
            else:
                for n in range(len(nums) - 1, 0, -1):
                    if nums[n] == sort[n]:
                        count += 1
                    else:
                        break
                break
        return len(nums) - count


# 2 Stack
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        min, max = nums[0], nums[0]
        for i in nums:
            if i > max: max = i
            if i < min: min = i
        stack1, stack2 = [], []
        if nums[0] == min:
            stack1 = [nums[0]]
            end = False
            for i in nums[1:]:
                if not end and  i >= stack1[-1]:
                    stack1.append(i)
                else:
                    while stack1 and stack1[-1] > i:
                        stack1.pop()
                    end = True
        if nums[-1] == max:
            stack2 = [nums[-1]]
            end = False
            for i in nums[-2::-1]:
                if not end and i <= stack2[-1]:
                    stack2.append(i)
                else:
                    while stack2 and stack2[-1] < i:
                        stack2.pop()
                    end = True
        if len(nums) == len(stack1):
            return 0
        else:
            return len(nums) - len(stack1) - len(stack2)