/*
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
*/


class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans;
        if (nums.empty()){
            ans.push_back(-1);
            ans.push_back(-1);
            return ans;
        }
        
        int lh = 0;
        int rh = nums.size()-1;
        while (0 <= lh && lh < rh && rh < nums.size()){
            int mid = lh + (rh - lh) / 2;
            if (target < nums[mid])
                rh = mid - 1;
            else if (target > nums[mid])
                lh = mid + 1;
            else
                rh = mid;
        }
        if (lh >= 0 and lh < nums.size() && nums[lh] == target)
            ans.push_back(lh);
        else
            ans.push_back(-1);
        
        lh = 0;
        rh = nums.size()-1;
        while (0 <= lh && lh < rh && rh < nums.size()){
            int mid = lh + (rh - lh + 1) / 2;
            if (target < nums[mid])
                rh = mid - 1;
            else if (target > nums[mid])
                lh = mid + 1;
            else
                lh = mid;
        }
        if (lh >= 0 and lh < nums.size() && nums[lh] == target)
            ans.push_back(lh);
        else
            ans.push_back(-1);
        
        return ans;
    }
};