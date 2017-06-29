class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum = 1
        if num%2==1 or num<1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sum += i + (0 if i*i==num else num/i)
        return sum==num
