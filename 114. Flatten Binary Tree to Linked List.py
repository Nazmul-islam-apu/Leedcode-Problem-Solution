# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        stack = []
        def helper(node,stack):
            if node is None:
                return
            if node.left:
                if node.right:
                    stack.append(node.right)
                node.right = node.left
                node.left = None
            if node.right:
                helper(node.right,stack)
            if stack:
                node.right = stack.pop()
                helper(node.right,stack)
        helper(root,stack)