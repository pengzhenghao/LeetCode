# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # recursive solution:
        self.ans = 0
        def f(node):
            if node==None:
                return 0
            else:
                l = f(node.left)
                r = f(node.right)
                self.ans += abs(l-r)
                return l+r+node.val
        f(root)
        return self.ans
        
