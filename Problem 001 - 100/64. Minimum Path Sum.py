class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        final = [[0 for _ in range(col)] for _ in range(row)]
        final[0][0] = grid[0][0]
        for i in range(1, row):
            final[i][0] = grid[i][0] + final[i - 1][0]
        for i in range(1, col):
            final[0][i] = grid[0][i] + final[0][i - 1]

        for i in range(1, row):
            for j in range(1, col):
                final[i][j] = min(final[i - 1][j], final[i][j - 1]) + grid[i][j]
        return final[row - 1][col - 1]