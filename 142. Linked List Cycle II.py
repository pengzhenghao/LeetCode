# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        flag = True
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast==slow:
                flag = False
                break
        if flag:
            return None
        fast = head
        while 1:
            if fast==slow:
                return fast
            fast = fast.next
            slow = slow.next

            
            
            
            
            
