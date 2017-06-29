# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:  return []
        stack = [root]
        result = []
        while stack!=[]:
            p = stack[-1]
            del stack[-1]
            l,r = p.left,p.right
            result.append(p.val)
            if p.right!=None:   stack.append(p.right)
            if p.left!=None:    stack.append(p.left)
        return result
