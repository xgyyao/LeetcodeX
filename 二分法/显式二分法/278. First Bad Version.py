# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        suc, err = 1, n
        while suc < err:
            test = (suc + err)//2
            if isBadVersion(test):
                err = test
            else:
                suc = test + 1
        return err