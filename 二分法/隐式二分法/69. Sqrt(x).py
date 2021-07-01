class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1:
            return 0
        if x<=3:
            return 1
        if x == 4:
            return 2
        l,r = 1, x//2
        while l<=r:
            mid = (l+r)//2
            if mid**2<= x and (mid+1)**2>x:
                return mid
            elif mid**2>x:
                r = mid
            else:
                l = mid+1
        return l