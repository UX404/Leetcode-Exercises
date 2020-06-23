'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.



Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2



Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2



Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.result = 0

        def collect(node):
            if not node: return 0
            lh = collect(node.left)
            rh = collect(node.right)
            if node.left and node.val == node.left.val:
                lh += 1
            else:
                lh = 0
            if node.right and node.val == node.right.val:
                rh += 1
            else:
                rh = 0
            self.result = max(self.result, lh + rh)
            return max(lh, rh)

        collect(root)
        return self.result