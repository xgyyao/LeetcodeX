class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        l, r = 0, nums_len - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]

