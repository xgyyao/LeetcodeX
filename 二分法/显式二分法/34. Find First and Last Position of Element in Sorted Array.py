class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return[-1, -1]
        res = []
        for index, val in enumerate(nums):
            if val == target:
                res.append(index)
        if len(res) == 1:
            return [res[0], res[0]]
        else:
            return [res[0], res[-1]]