# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:    return head
        tmp = head
        for _ in range(k):
            if tmp==None:
                return head
            tmp = tmp.next
        result,next = self.reverse(head,k)
        head.next = self.reverseKGroup(next,k)
        return result

    def reverse(self,node,k):
        p = q = node
        r = ListNode(0)
        for _ in range(k):
            q = p.next
            p.next = r.next
            r.next = p
            p = q
        return r.next,p

                
