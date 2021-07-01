# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        final = []
        stack1 = [];
        stack2 = []
        stack1.append(root)
        while (stack1 or stack2):
            pre = []
            while (stack1):
                temp = stack1.pop(0)
                pre.append(temp.val)
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)
            if (len(pre) > 0):
                final.append(pre)
            pre = []
            while (stack2):
                temp = stack2.pop(0)
                pre.append(temp.val)
                if temp.left:
                    stack1.append(temp.left)
                if temp.right:
                    stack1.append(temp.right)

            if (len(pre) > 0):
                final.append(pre)

        final.reverse()
        return final