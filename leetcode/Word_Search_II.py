import collections


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        #approach
        #1. use recursion to find the words in the board
        #time complexity
        #1. O(n) where n is the number of words
        #space complexity
        #1. O(n) where n is the number of words
        result = set()
        for word in words:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if self.dfs(board, row, col, word):
                        result.add(word)
        return list(result)

    def dfs(self, board, row, col, word):
        if not word:
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[0]:
            return False
        temp = board[row][col]
        board[row][col] = '#'
        result = self.dfs(board, row + 1, col, word[1:]) or self.dfs(board, row - 1, col, word[1:]) or self.dfs(board, row, col + 1, word[1:]) or self.dfs(board, row, col - 1, word[1:])
        board[row][col] = temp
        return result

#         #Given an m x n board of characters and a list of strings words, return all words on the board.
#         #Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#         #Example 1:
#         #Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
#         #Output: ["eat","oath"]
    
