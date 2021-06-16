# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = list()
        self.inorderTraversalHelper(root, l)
        return l

    def inorderTraversalHelper(self, node, l):
        if node:
            if node.left:
                self.inorderTraversalHelper(node.left, l)

            l.append(node.val)

            if node.right:
                self.inorderTraversalHelper(node.right, l)