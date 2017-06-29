class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,j in enumerate(nums):
            if dic.has_key(j):
                return [dic[j],i]
            else:
                dic[target-j] = i
