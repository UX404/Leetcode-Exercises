'''
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root.left:
            difference = abs(root.val - root.left.val)
        else:
            difference = abs(root.val - root.right.val)
        temp = None

        def midorder(node):
            if not node: return
            nonlocal temp, difference
            midorder(node.left)
            if temp == None:
                temp = node.val
            else:
                difference = min(difference, abs(temp - node.val))
                temp = node.val
            midorder(node.right)

        midorder(root)
        return difference