# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return
        temp1 = l1
        temp2 = l2
        if temp1.val < temp2.val:
            final = ListNode(temp1.val)
            temp1 = temp1.next
        else:
            final = ListNode(temp2.val)
            temp2 = temp2.next
        temp = final

        while (temp1 or temp2):
            if temp1 and temp2:
                if temp1.val < temp2.val:
                    temp.next = ListNode(temp1.val)
                    temp = temp.next
                    temp1 = temp1.next
                else:
                    temp.next = ListNode(temp2.val)
                    temp = temp.next
                    temp2 = temp2.next
            else:
                if temp1:
                    while (temp1):
                        temp.next = ListNode(temp1.val)
                        temp = temp.next
                        temp1 = temp1.next
                else:
                    while (temp2):
                        temp.next = ListNode(temp2.val)
                        temp = temp.next
                        temp2 = temp2.next
        return final