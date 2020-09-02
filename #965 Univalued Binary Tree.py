'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.



Example 1:


Input: [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: [2,2,2,5,2]
Output: false


Note:

The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1 Recursion
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root.left and root.right:
            return root.val == root.left.val == root.right.val and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        elif root.left:
            return root.val == root.left.val and self.isUnivalTree(root.left)
        elif root.right:
            return root.val == root.right.val and self.isUnivalTree(root.right)
        else:
            return True


# 2 Iteration
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        sample = root.val
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp:
                if temp.val != sample:
                    return False
                stack.append(temp.left)
                stack.append(temp.right)
        return True