# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p = r = ListNode(val-1)
        r.next = head
        while p and p.next:
            q = p.next
            if q.val==val:
                p.next = q.next
                del q
                continue
            p = p.next
        return r.next
        
