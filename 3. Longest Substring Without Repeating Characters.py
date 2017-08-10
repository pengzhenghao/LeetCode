class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        ans = 0
        sub = ''
        for c in s:
            for i in range(-1,-len(sub)-1,-1):
                if sub[i]==c:
                    ans = max(ans,len(sub))
                    sub = sub[len(sub)+i+1:]
                    break
            sub += c
        return max(ans,len(sub))
        '''
        # DP solution
        dic = [-1]*256
        ans = left = 0
        for right,c in enumerate(s):
            left = max(dic[ord(c)]+1,left)
            dic[ord(c)] = right
            ans = max(ans,right-left+1)
        return ans
                
            
            
            
            
            
            
            
