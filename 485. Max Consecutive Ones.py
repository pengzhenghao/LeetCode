class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = tmp = 0
        for i in nums:
            if i:
                tmp += 1
            else:
                ma = max(ma,tmp)
                tmp = 0
        ma = max(ma,tmp)
        return ma
