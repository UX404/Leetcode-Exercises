'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 1 Recursion
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def judge_return(node, isLeft):
            if not node: return 0
            if isLeft and not node.left and not node.right:
                return node.val + judge_return(node.right, False)
            else:
                return judge_return(node.left, True) + judge_return(node.right, False)
        return judge_return(root, False)


# 2 Iteration
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue = [(root, False)]
        left_sum = 0
        while queue:
            head = queue.pop(0)
            if head[0]:
                if head[1] and not head[0].left and not head[0].right: left_sum += head[0].val
                queue.append((head[0].left, True))
                queue.append((head[0].right, False))
            else: continue
        return left_sum