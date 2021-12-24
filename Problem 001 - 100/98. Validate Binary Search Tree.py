# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = [(root,float('-inf'),float('inf'))]
        while stack:
            temp,lower,upper = stack.pop()
            if temp is None:
                continue
            if temp.val<=lower or temp.val>=upper:
                return False
            stack.append((temp.right,temp.val,upper))
            stack.append((temp.left,lower,temp.val))
        return True