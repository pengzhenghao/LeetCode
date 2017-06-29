# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r,s = [],[]
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                return r
            n = s.pop()
            r.append(n.val)
            root = n.right
