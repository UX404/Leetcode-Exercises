'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        result = []
        nodes = [root]
        paths = [str(root.val)]
        while nodes:
            node = nodes.pop()
            path = paths.pop()
            if node.left:
                nodes.append(node.left)
                paths.append(path + "->" + str(node.left.val))
            if node.right:
                nodes.append(node.right)
                paths.append(path + "->" + str(node.right.val))
            if not node.left and not node.right:
                result.append(path)
        return result