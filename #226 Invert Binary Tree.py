'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invent a binary tree on a whiteboard so f*** off.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Iteration
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        level = [root]
        while level:
            p = level.pop(0)
            temp = p.left
            p.left = p.right
            p.right = temp
            if p.left: level.append(p.left)
            if p.right: level.append(p.right)
        return root


# 2 Recursion
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        else:
            temp1 = self.invertTree(root.left)
            temp2 = self.invertTree(root.right)
            root.left = temp2
            root.right = temp1
            return root