class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x+y<z: return False
        if z==x or y==z or z==x+y: return True
        while y!=0:
            y,x = x%y,y
        return not z%x
