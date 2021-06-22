# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        stack1 = []
        stack2 = []
        final = []
        stack1.append(root)
        while (stack1 or stack2):
            new = []
            while (stack1):
                temp = stack1.pop(0)
                new.append(temp.val)
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)

            if (new):
                final.append(new)
            new = []
            while (stack2):
                temp = stack2.pop(0)
                new.append(temp.val)
                if temp.left:
                    stack1.append(temp.left)
                if temp.right:
                    stack1.append(temp.right)
            if (new):
                final.append(new[::-1])
        return final  