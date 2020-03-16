'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0 : return None
        elif len(nums) == 1 : return TreeNode(nums[0])
        else:
            mid = int(len(nums) / 2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[0: mid])
            root.right = self.sortedArrayToBST(nums[mid+1: len(nums)])
            return root


# Failure
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        len0 = len(nums)
        if len0 == 0 : return None
        mid = int((len0-1) / 2)
        root = TreeNode(nums[mid])
        if len0 == 1 : return root
        root.right = TreeNode(nums[-1])
        p = root
        for n in range(mid-1, -1, -1):
            p.left = TreeNode(nums[n])
            p = p.left
        p = root.right
        for n in range(len0-2, mid, -1):
            p.left = TreeNode(nums[n])
            p = p.left
        return root