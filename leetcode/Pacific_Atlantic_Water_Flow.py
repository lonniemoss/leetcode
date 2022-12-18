import collections


class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = []
        # check if the matrix is empty
        if not heights:
            return ret
        # get the row and column of the matrix
        row = len(heights)
        col = len(heights[0])
        # create two matrix to store the result
        pacific = [[False] * col for _ in range(row)]
        atlantic = [[False] * col for _ in range(row)]
        # create two queue to store the coordinate
        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()
        # traverse the first and last row
        for i in range(col):
            pacific_queue.append((0, i))
            atlantic_queue.append((row - 1, i))
        # traverse the first and last column
        for i in range(row):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, col - 1))
        # bfs the pacific ocean
        while pacific_queue:
            x, y = pacific_queue.popleft()
            pacific[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and not pacific[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    pacific_queue.append((nx, ny))
        # bfs the atlantic ocean
        while atlantic_queue:
            x, y = atlantic_queue.popleft()
            atlantic[x][y] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col and not atlantic[nx][ny] and heights[nx][ny] >= heights[x][y]:
                    atlantic_queue.append((nx, ny))
        # traverse the matrix to find the result
        for i in range(row):
            for j in range(col):
                if pacific[i][j] and atlantic[i][j]:
                    ret.append([i, j])
        return ret
        #Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
        #Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
        #Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
        #Note:
        #The order of returned grid coordinates does not matter.
        #Both m and n are less than 150.
        #Example:
        #Given the following 5x5 matrix:
        #  Pacific ~   ~   ~   ~   ~
        #       ~  1   2   2   3  (5) *
        #       ~  3   2   3  (4) (4) *
        #       ~  2   4  (5)  3   1  *
        #       ~ (6) (7)  1   4   5  *
        #       ~ (5)  1   1   2   4  *
        