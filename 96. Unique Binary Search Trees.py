class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:return 1
        re = [1]*(n+1)
        for i in range(2,n+1):
            re[i] = sum([re[k-1]*re[i-k] for k in range(1,i+1)])
        return re[n]
