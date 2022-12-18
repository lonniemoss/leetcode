class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #approach
        #1. use four pointers to indicate the boundaries of the matrix
        #2. traverse the matrix in a spiral order
        #time complexity
        #1. O(mn) where m is the number of rows and n is the number of columns
        #space complexity
        #1. O(1) constant space
        
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # spiral matrix
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        ret = []
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                ret.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                ret.append(matrix[i][right])
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    ret.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    ret.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return ret
        #Given an m x n matrix, return all elements of the matrix in spiral order.