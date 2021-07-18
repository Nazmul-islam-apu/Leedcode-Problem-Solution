# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            return max(lh,rh)+1
        if root is None:
            return True
        stack = []
        stack.append(root)
        while(stack):
            temp = stack.pop()
            left_height = height(temp.left)
            right_height = height(temp.right)
            if abs(left_height-right_height)>1:
                return False
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return True