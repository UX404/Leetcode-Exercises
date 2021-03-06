'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.


Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def checkSame(root1, root2):
            if not root1 or not root2:
                if not root1 and not root2:
                    return True
                else:
                    return False
            if not checkSame(root1.left, root2.left): return False
            if not root1.val == root2.val: return False
            if not checkSame(root1.right, root2.right): return False
            return True

        level = [s]
        while level:
            for i in level:
                if i.val == t.val:
                    if checkSame(i, t):
                        return True
            level = [i.left for i in level if i.left] + [i.right for i in level if i.right]
        return False