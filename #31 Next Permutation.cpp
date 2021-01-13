/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
*/


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int p = nums.size() - 1;
        while (p > 0){
            if (nums[p-1] < nums[p]){
                for(int i = nums.size()-1; i >= p; i --){
                    if (nums[i] > nums[p-1]){
                        int temp = nums[p-1];
                        nums[p-1] = nums[i];
                        nums[i] = temp;
                        break;
                    }
                }
                break;
            }
            p --;
        }
        for (int i = p; i <= p+(nums.size()-1-p)/2; i ++){
            int temp = nums[i];
            nums[i] = nums[nums.size()-1-i+p];
            nums[nums.size()-1-i+p] = temp;
        }
    }
};