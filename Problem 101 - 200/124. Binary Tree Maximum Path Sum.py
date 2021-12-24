# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def helper(node):
            if node is None:
                return 0
            ln = helper(node.left)
            rn = helper(node.right)
            max_single = max(max(ln, rn) + node.val, node.val)
            max_top = max(max_single, ln + rn + node.val)
            helper.res = max(helper.res, max_top)
            return max_single

        helper.res = float("-inf")
        helper(root)
        return helper.res