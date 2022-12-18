class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = [0] * (amount + 1)
        for i in range(1, amount + 1):
            ret[i] = MAX
            for j in range(len(coins)):
                if i >= coins[j] and ret[i - coins[j]] != MAX:
                    ret[i] = min(ret[i], ret[i - coins[j]] + 1)
        return ret[amount] if ret[amount] != MAX else -1
        #You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
        #You may assume that you have an infinite number of each kind of coin.