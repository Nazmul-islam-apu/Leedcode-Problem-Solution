# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        order = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            order.append(root)
            inorder(root.right)

        inorder(root)

        new = sorted(order, key=lambda x: x.val)

        l = len(order)

        for i in range(l):
            p, q = order[i], new[i]
            if p != q:
                p.val, q.val = q.val, p.val
                break