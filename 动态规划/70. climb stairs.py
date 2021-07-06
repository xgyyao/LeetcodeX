class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        f1 = 1
        f2 = 2
        while(n>2):
            fn = f1+f2
            f1 = f2
            f2 = fn
            n -= 1
        return fn