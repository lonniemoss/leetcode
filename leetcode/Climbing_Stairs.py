class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = 1
        b = 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
        #You are climbing a staircase. It takes n steps to reach the top.
        #Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
        