'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0
        def depth(node):
            if not node: return 0
            nonlocal diameter
            lh = depth(node.left)
            rh = depth(node.right)
            diameter = max(diameter, lh+rh)
            return max(lh, rh) + 1
        depth(root)
        return diameter


# Error: It's possible that the left branch is very short while the right branch has two long branches
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        lh, rh = 0, 0
        if root.left:
            lt = [root.left]
            while lt:
                lt = [i.left for i in lt if i.left] + [i.right for i in lt if i.right]
                lh += 1
        if root.right:
            rt = [root.right]
            while rt:
                rt = [i.left for i in rt if i.left] + [i.right for i in rt if i.right]
                rh += 1
        return lh + rh