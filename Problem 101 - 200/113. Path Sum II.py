# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def rootToleaf(root, stack, path, s):
    if root is not None:
        stack.append(root.val)
        rootToleaf(root.left, stack, path, s)
        rootToleaf(root.right, stack, path, s)

        if root.left is None and root.right is None:
            if sum(stack) == s:
                path.append(stack[::])
        stack.pop()
    return path


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        stack = []
        path = []
        return (rootToleaf(root, stack, path, sum))