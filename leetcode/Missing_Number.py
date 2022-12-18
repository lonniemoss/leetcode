class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
          # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        for i in range(len(nums)):
            ret ^= i
            ret ^= nums[i]
        ret ^= len(nums)
        return ret
        #Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.