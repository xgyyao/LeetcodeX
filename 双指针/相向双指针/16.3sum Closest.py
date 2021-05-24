class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = 1000000
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len - 2):
            p1 = i + 1
            p2 = nums_len - 1
            while(p1 < p2):
                sum = nums[i] + nums[p1] + nums[p2]
                new_diff = sum - target
                if abs(new_diff) < diff:
                    diff = abs(new_diff)
                    if new_diff < 0:
                        diff_flag = -1
                    if new_diff > 0:
                        diff_flag = 1
                if new_diff > 0:
                    p2 -= 1
                if new_diff < 0:
                    p1 += 1
                if new_diff == 0:
                    return target
        return diff * diff_flag + target

