class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        res = 0
        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i]==nums[j]:
                    res += 1
        return res