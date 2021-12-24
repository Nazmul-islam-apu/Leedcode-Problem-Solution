# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def rootToleaf(root, stack, l, s):
    if root is not None:
        stack.append(root.val)
        rootToleaf(root.left, stack, l, s)
        rootToleaf(root.right, stack, l, s)
        if root.left is None and root.right is None:
            l.append(sum(stack))
        stack.pop()
    return l


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        stack = []
        l = []
        l = rootToleaf(root, stack, l, sum)
        if sum in l:
            return True
        else:
            return False