class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        minimum = [x[0] for x in arrays]
        maximum = [x[-1] for x in arrays]
        return max(maximum)-min(minimum)
