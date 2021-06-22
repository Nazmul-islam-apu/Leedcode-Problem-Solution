# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        hL = self.maxDepth(root.left)
        hR = self.maxDepth(root.right)
        if(hL>hR):
            return 1+hL
        else:
            return 1+hR