class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high)//2
            if arr[mid] < arr[mid+1]:
                low = mid+1
            else:
                high = mid
        return low
