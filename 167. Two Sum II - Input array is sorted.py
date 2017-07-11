class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = [0, 1]
        while numbers[l[0]]+numbers[-1*l[1]]!=target:
            l[numbers[l[0]]+numbers[-1*l[1]]>target] += 1
        return [l[0]+1,len(numbers)-l[1]+1]
            
