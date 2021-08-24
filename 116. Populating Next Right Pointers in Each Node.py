"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return
        stack1 = []
        stack2 = []
        stack1.append(root)
        while (stack1 or stack2):
            while (stack1):
                temp = stack1.pop(0)
                if temp.left:
                    if stack2:
                        stack2[-1].next = temp.left
                    stack2.append(temp.left)
                if temp.right:
                    if stack2:
                        stack2[-1].next = temp.right
                    stack2.append(temp.right)
            temp.next = None
            while (stack2):
                temp = stack2.pop(0)
                if temp.left:
                    if stack1:
                        stack1[-1].next = temp.left
                    stack1.append(temp.left)
                if temp.right:
                    if stack1:
                        stack1[-1].next = temp.right
                    stack1.append(temp.right)
            temp.next = None
        return root
