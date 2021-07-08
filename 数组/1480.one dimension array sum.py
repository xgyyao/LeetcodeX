class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        res = []
        if len(nums) == 0:
            return []
        for num in nums:
            sum += num
            res.append(sum)
        return res