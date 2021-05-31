class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        if n > 1:
            return self.isPowerOfFour(n / 4)