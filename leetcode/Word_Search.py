class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #approach
        #1. find the first letter in the board
        #2. find the next letter in the board
        #3. repeat 2 until the word is found
        #time complexity
        #1. O(n^2) where n is the number of rows in the board
        #space complexity
        #1. O(n) where n is the number of rows in the board
        
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # dfs
        def dfs(i, j, k):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = '#'
            ret = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return ret
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
        #Given an m x n board and a word, find if the word exists in the grid.