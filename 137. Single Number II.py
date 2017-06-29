class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        o = t = 0
        for i in nums:
            o = (o^i) & (~t)
            t = (t^i) & (~o)
        return o
