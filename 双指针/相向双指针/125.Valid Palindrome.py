class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_len = len(s)
        p1 = 0
        p2 = s_len - 1
        while(p1 < p2):
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
                continue
            if s[p1] != s[p2]:
                break
        if p1 < p2:
            return False
        else:
            return True

