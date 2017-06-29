class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-1)
        for ind in range(len(nums)):
            real = nums[ind]
            while real>=0 and real<len(nums) and real!=nums[real]:
                nums[real],real = real,nums[real]
        for i in range(1,len(nums)):
            if nums[i]!=i:  return i
        return len(nums)
