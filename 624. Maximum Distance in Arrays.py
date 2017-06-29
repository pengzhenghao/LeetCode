class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min,imin,amin = [arrays[0][0],0,arrays[1][0]] if arrays[0][0]<arrays[1][0] else [arrays[1][0],1,arrays[0][0]]
        max,imax,amax = [arrays[0][-1],0,arrays[1][-1]] if arrays[0][-1]>arrays[1][-1] else [arrays[1][-1],1,arrays[0][-1]]
        for ind in range(2,len(arrays)):
            if arrays[ind][0]<min:
                amin,min,imin = min,arrays[ind][0],ind
            elif arrays[ind][0]<amin:
                amin = arrays[ind][0]
            if arrays[ind][-1]>max:
                amax,max,imax = max,arrays[ind][-1],ind
            elif arrays[ind][-1]>amax:
                amax = arrays[ind][-1]
        if imin==imax:
            return max-amin if max-amin>amax-min else amax-min
        return max-min
                
