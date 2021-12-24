# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return
        count = 0
        temp = head
        while(temp):
            count+=1
            temp = temp.next
        target = count-n
        if target ==0:
            temp = head
            head = temp.next
            temp = None
            return head
        new = 0
        temp = head
        while(new<target):
            new+=1
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None
        return head