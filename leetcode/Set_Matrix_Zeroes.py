class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #approach
        #1. use the first row and first column to store the information of the rest of the matrix
        #2. if the first row or first column has a zero, set the corresponding row or column to zero
        #3. set the first row and first column to zero if necessary
        #time complexity
        #1. O(mn) where m is the number of rows and n is the number of columns
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
        # flag to indicate if the first row has a zero
        first_row = False
        # flag to indicate if the first column has a zero
        first_col = False
        # check if the first row has a zero
        for i in range(n):
            if matrix[0][i] == 0:
                first_row = True
                break
        # check if the first column has a zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
                break
        # use the first row and first column to store the information of the rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # set the corresponding row or column to zero
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # set the first row and first column to zero if necessary
        if first_row:
            for i in range(n):
                matrix[0][i] = 0
        if first_col:
            for i in range(m):
                matrix[i][0] = 0
        #Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
        