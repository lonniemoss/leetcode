class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
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
        # dp list
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        return dp[target]
        #Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
        #Example:
        #nums = [1, 2, 3]
        #target = 4
        #The possible combination ways are:
        #(1, 1, 1, 1)
        #(1, 1, 2)
        #(1, 2, 1)
        #(1, 3)
        #(2, 1, 1)
        #(2, 2)
        #(3, 1)
        #Note that different sequences are counted as different combinations.
        #Therefore the output is 7.
        #Follow up:
        #What if negative numbers are allowed in the given array?
        #How does it change the problem?
        #What limitation we need to add to the question to allow negative numbers?
        #Credits:
        #Special thanks to @pbrother for adding this problem and creating all test cases.