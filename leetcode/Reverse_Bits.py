class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        for i in range(32):
            ret = (ret << 1) + (n & 1)
            n = n >> 1
        return ret
        #Reverse bits of a given 32 bits unsigned integer.
        # 
        # 
        # 
        # Example 1:
        # 
        # Input: 000000101001