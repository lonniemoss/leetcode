class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # dp list
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i - 1] - 1, nums[i])
            if dp[i] == 0 and i != len(nums) - 1:
                return False
        return True
        #Given an array of non-negative integers, you are initially positioned at the first index of the array.
        #Each element in the array represents your maximum jump length at that position.
        #Determine if you are able to reach the last index.