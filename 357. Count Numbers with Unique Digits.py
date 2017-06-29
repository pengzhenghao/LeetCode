class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        '''___________________
        if n>10:    return 0
        if n==0:    return 1
        if n==1:    return 10
        
        def fact(x,y):
            if y==0:    return 1
            if x==0:    return 1
            return x*fact(x-1,y-1)
            
        return 9*fact(9,n-1)+self.countNumbersWithUniqueDigits(n-1)
        '''___________________
        
        
        return 0 if n>10 else {0:1,1:10,2:91,3:739,4:5275,5:32491,6:168571,7:712891,8:2345851,9:5611771,10:8877691}[n]
