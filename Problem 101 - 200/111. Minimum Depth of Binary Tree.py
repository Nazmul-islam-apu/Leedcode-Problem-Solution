# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = []
        queue.append({'node': root, 'depth': 1})

        while (queue):
            temp = queue.pop(0)
            node = temp['node']
            depth = temp['depth']

            if node.left is None and node.right is None:
                return depth

            if node.left is not None:
                queue.append({'node': node.left, 'depth': depth + 1})

            if node.right is not None:
                queue.append({'node': node.right, 'depth': depth + 1})
