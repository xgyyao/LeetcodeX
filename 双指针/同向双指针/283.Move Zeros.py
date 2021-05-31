class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if nums_len < 2:
            return nums
        count = 0
        for i in range(nums_len):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        for i in range(count, nums_len):
            nums[i] = 0
        return nums