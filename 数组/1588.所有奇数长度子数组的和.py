class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        pre = [0] * n
        summ = 0
        # 计算前缀和
        for i in range(n):
            summ += arr[i]
            pre[i] = summ
        # 计算奇数数组和
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if (j - i) % 2 == 0:
                    ans += pre[j] - pre[i] + arr[i]
        return ans

