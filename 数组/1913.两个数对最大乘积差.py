class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = nums[-1]*nums[-2] - nums[0]*nums[1]
        return res