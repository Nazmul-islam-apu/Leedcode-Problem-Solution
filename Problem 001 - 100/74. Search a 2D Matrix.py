class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            return

        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        x = -1

        for i in range(0, m):
            if target >= matrix[i][0] and target < matrix[i + 1][0]:
                x = i

        if target >= matrix[m][0]:
            x = m
        lo = 0;
        hi = n
        while (lo < hi):
            mid = (lo + hi) // 2
            if matrix[x][mid] > target:
                hi = mid - 1
            elif matrix[x][mid] < target:
                lo = mid + 1
            else:
                return True
        if x == -1:
            return False

        if (lo == hi):
            if matrix[x][lo] == target:
                return True
            else:
                return False
        return False
