class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        len_row, len_col = len(matrix), len(matrix[0])
        l, r = 0, len_row - 1
        while(l<r):
            mid = (l+r+1)//2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid - 1
        row = l
        l,r = 0, len_col - 1
        while(l<r):
            mid = (l+r+1)//2
            if matrix[row][mid]<=target:
                l = mid
            else:
                r = mid - 1
        return target == matrix[row][l]