'''
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.



Constraints:

Both of the given trees will have between 1 and 200 nodes.
Both of the given trees will have values between 0 and 200
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_sequence(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            return get_sequence(root.left) + get_sequence(root.right)

        return get_sequence(root1) == get_sequence(root2)