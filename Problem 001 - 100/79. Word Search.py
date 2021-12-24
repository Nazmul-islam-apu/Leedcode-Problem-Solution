class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False

            if k == len(word) - 1:
                return True

            board[i][j] = "#"
            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                    if dfs(new_i, new_j, k + 1):
                        return True
            board[i][j] = word[k]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False