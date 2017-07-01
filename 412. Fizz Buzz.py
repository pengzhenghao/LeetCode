class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return [ str(x) if x%5!=0 and x%3!=0 else "FizzBuzz" if x%3==x%5 else "Fizz" if x%3==0 else "Buzz" for x in range(1,n+1)]
