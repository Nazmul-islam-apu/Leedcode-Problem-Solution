# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def rootToleaf(root, stack, path_num):
    if root is not None:
        stack.append(root.val)

        rootToleaf(root.left, stack, path_num)
        rootToleaf(root.right, stack, path_num)

        if root.left is None and root.right is None:
            s = "".join(map(str, stack))
            path_num.append(s)
        stack.pop()
    return path_num


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        path_num = []
        path_num = rootToleaf(root, stack, path_num)
        final = 0
        for i in path_num:
            final += int(i)
        return final