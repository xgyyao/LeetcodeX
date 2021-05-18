class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_length = len(numbers)
        p1 = 0
        p2 = nums_length - 1
        while(1):
            sum = numbers[p1] + numbers[p2]
            if sum < target:
                p1 += 1
            if sum > target:
                p2 -= 1
            if sum == target:
                return [p1+1, p2+1]