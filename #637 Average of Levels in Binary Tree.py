'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 1 BFS
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        level = [root]
        value = []
        result = []
        while level:
            value = [i.val for i in level]
            result.append(sum(value) / len(value))
            level = [i.left for i in level if i.left] + [i.right for i in level if i.right]
        return result


# 2 DFS
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        num_sum = []
        num_size = []

        def preorder(node, index):
            if not node: return
            nonlocal num_sum, num_size
            if len(num_size) <= index:
                num_sum.append(0)
                num_size.append(0)
            num_sum[index] += node.val
            num_size[index] += 1
            preorder(node.left, index + 1)
            preorder(node.right, index + 1)

        preorder(root, 0)
        return [num_sum[n] / num_size[n] for n in range(len(num_sum))]