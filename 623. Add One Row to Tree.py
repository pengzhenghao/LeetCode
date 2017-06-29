# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            new = TreeNode(v)
            new.left = root
            return new
        l = [root]
        for _ in range(2,d):
            width = len(l)
            for i in range(width):
                if l[i].left:   l.append(l[i].left)
                if l[i].right:  l.append(l[i].right)
            del l[:width]
        for node in l:
            tl,tr = TreeNode(v),TreeNode(v)
            tl.left,tr.right = node.left,node.right
            node.left,node.right = tl,tr
        return root
        
            
        
        
        
        
        
        
