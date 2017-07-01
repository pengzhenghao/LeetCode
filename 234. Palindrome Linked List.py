# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None:  return True
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse(slow.next) if fast else self.reverse(slow)
        while(slow):
            if slow.val!=head.val:  return False
            head = head.next
            slow = slow.next
        return True
    
    def reverse(self, node):
        p = node
        r = ListNode(0)
        while p:
            q = p.next
            p.next = r.next
            r.next = p
            p = q
        return r.next
