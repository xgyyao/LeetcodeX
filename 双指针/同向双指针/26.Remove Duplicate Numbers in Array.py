class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len < 2:
            return nums_len
        Pslow = 0
        Pfast = 1

        while Pfast < nums_len:
            if nums[Pslow] == nums[Pfast]:
                Pfast += 1
            else:
                nums[Pslow+1], nums[Pfast] = nums[Pfast],nums[Pslow+1]
                Pfast += 1
                Pslow += 1
        del nums[Pslow+1:]
        return len(nums)

    