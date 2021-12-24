# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None:
            if q is None:
                return True
            else:
                return False
        elif q is None:
            if p is None:
                return True
            else:
                return False

        stack1 = [];
        stack2 = []
        stack1.append(p);
        stack2.append(q)
        while (stack1 or stack2):
            temp1, temp2 = stack1.pop(0), stack2.pop(0)

            if temp1.val == temp2.val:
                if (temp1.left and temp2.left):
                    stack1.append(temp1.left)
                    stack2.append(temp2.left)
                else:
                    if (temp1.left is None and temp2.left is not None) or (
                            temp1.left is not None and temp2.left is None):
                        return False

                if (temp1.right and temp2.right):
                    stack1.append(temp1.right)
                    stack2.append(temp2.right)
                else:
                    if (temp1.right is None and temp2.right is not None) or (
                            temp1.right is not None and temp2.right is None):
                        return False

            else:
                return False
        return True
