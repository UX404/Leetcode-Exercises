'''

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1 Recursion
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        count = 0

        def reverseorder(node):
            if not node: return
            nonlocal count
            reverseorder(node.right)
            node.val += count
            count = node.val
            reverseorder(node.left)

        reverseorder(root)
        return root


# 2 Stack
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = [root]
        count = 0
        while stack:
            node = stack[-1]
            while node:
                stack.append(node.right)
                node = stack[-1]
            stack.pop()
            if stack:
                node = stack.pop()
                count += node.val
                node.val = count
                stack.append(node.left)
        return root