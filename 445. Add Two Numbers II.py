# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = 0
        tmp1, tmp2 = l1, l2
        while tmp1!=None:
            num1 = tmp1.val + 10 * num1
            tmp1 = tmp1.next
        while tmp2!=None:
            num2 = tmp2.val + 10 * num2
            tmp2 = tmp2.next
        result = num1 + num2
        if result==0:
            return ListNode(0)
        node = None
        while result:
            tmpnode = ListNode(result%10)
            tmpnode.next = node
            node = tmpnode
            result = result // 10
        return node
