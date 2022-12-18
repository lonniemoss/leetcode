class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #approach
        #1. transpose the matrix
        #2. reverse each row
        #time complexity
        #1. O(n^2) where n is the number of rows and columns
        #space complexity
        #1. O(1) constant space
        #edge case
        if not matrix:
            return
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # number of rows
        m = len(matrix)
        # number of columns
        n = len(matrix[0])
        # transpose the matrix
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse each row
        for i in range(m):
            matrix[i].reverse()
        #Given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).