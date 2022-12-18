class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
    #Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
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
        def helper(nums):
            ret = 0
            dp = [0] * len(nums)
            for i in range(len(nums)):
                if i == 0:
                    dp[i] = nums[i]
                elif i == 1:
                    dp[i] = max(nums[0], nums[1])
                else:
                    dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
                ret = max(ret, dp[i])
            return ret
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))