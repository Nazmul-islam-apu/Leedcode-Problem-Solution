# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queue = []
        queue.append(root);
        queue.append(root)
        while (queue):
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if (t1 is None and t2 is None):
                continue

            if (t1 is None or t2 is None):
                return False

            if (t1.val != t2.val):
                return False

            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

        return True