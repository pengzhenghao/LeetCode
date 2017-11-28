class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        r, l, k = [[]], 1, 0
        while k<len(nums):
            for i in range(l):
                p = r[i]
                anum = nums[k]
                for j in range(len(p)+1):
                    r.append(p[:j]+[anum]+p[j:])
            del r[:l]
            l = len(r)
            k += 1
        return r
            
