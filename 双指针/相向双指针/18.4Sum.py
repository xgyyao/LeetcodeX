class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        res = []
        if nums_len < 4:
            return res
        nums.sort()
        for i in range(nums_len - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, nums_len - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p1 = j + 1
                p2 = nums_len - 1
                while (p1 < p2):
                    sum = nums[i] + nums[j] + nums[p1] + nums[p2]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[p1], nums[p2]])
                        while (p1 < p2 and nums[p1] == nums[p1 + 1]):
                            p1 += 1
                        while (p1 < p2 and nums[p2] == nums[p2 - 1]):
                            p2 -= 1
                        p1 += 1
                        p2 -= 1
                    elif sum < target:
                        p1 += 1
                    elif sum > target:
                        p2 -= 1
        return res



