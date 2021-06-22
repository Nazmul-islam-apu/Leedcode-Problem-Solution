# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return
        queue = [];
        return_list = []
        queue.append(root)
        while (len(queue) > 0):
            l = len(queue);
            ans = []
            for i in range(l):
                temp = queue.pop(0)
                ans.append(temp.val)
                if (temp.left):
                    queue.append(temp.left)
                if (temp.right):
                    queue.append(temp.right)
            return_list.append(ans)
        return return_list
