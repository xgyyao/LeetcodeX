# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        while a != b:
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a