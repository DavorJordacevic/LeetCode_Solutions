# https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True

        return False

    def dfs(self, board, word, row, col, k):
        if k == len(word):
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[k]:
            return False

        temp = board[row][col]
        board[row][col] = '#'

        if self.dfs(board, word, row+1, col, k+1) or self.dfs(board, word, row-1, col, k+1) or self.dfs(board, word, row, col+1, k+1) or self.dfs(board, word, row, col-1, k+1):
                return True
        board[row][col] = temp
        return False

        