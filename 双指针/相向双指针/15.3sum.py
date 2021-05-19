class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_length = len(nums)
        res = []
        if nums_length < 3:
            return res
        nums.sort()
        for i in range(nums_length - 2):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            if nums[i] > 0:
                return res
            target = -nums[i]
            p1 = i + 1
            p2 = nums_length - 1
            while(p1<p2):
                if nums[p1] + nums[p2] == target:
                    res.append([nums[i], nums[p1], nums[p2]])
                    while(p1 < p2 and nums[p1] == nums[p1+1]):
                        p1 += 1
                    while(p1< p2 and nums[p2] == nums[p2-1]):
                        p2 -= 1
                    p1 += 1
                    p2 -= 1
                elif nums[p1] + nums[p2] < target:
                    p1 += 1
                elif nums[p1] + nums[p2] > target:
                    p2 -= 1
        return res