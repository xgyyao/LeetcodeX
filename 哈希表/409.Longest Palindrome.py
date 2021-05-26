class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        dic = {}
        res = 0
        odd_flag = 0
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1
        for value in dic.values():
            if value % 2 == 0:
                res += value
            if value % 2 == 1:
                res += value - 1
                odd_flag = 1
        return res + odd_flag