class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        count = 0
        while n != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            n = (n & (n - 1))
            count += 1
        # if a is negative, get a's 32 bit complement positive first
        # then get a's 32 bit complement positive
        return count