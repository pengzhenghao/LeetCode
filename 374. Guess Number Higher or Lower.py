# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b,c = 1,n,(1+n)//2
        while c!=a:
            a,b = [c,b] if guess(c)==1 else [a,c]
            c = (a+b)//2
        return a if guess(a)==0 else b
