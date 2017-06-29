# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:  return []
        s,re = [root],[]
        while s!=[]:
            p = s[-1]
            del s[-1]
            l,r = p.left,p.right
            if l: s.append(l)
            if r: s.append(r)
            re.append(p.val)
        return re[::-1]
