# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.f(1,n) if n else []
        
    def f(self, s, e):
        if s>e:
            return [None]
        re = []
        for i in range(s,e+1):
            leftSub = self.f(s,i-1)
            rightSub = self.f(i+1,e)
            for l in leftSub:
                for r in rightSub:
                    head = TreeNode(i)
                    head.left = l
                    head.right = r
                    re.append(head)
        return re
            
            
