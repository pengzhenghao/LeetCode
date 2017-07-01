# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        re = 0
        s = [root]
        while s:
            if s[0].left and not s[0].left.left and not s[0].left.right:
                re += s[0].left.val
            if s[0].left:
                s.append(s[0].left)
            if s[0].right:
                s.append(s[0].right)
            del s[0]
        return re
