class Solution(object):
    def longestConsecutive(self, nums):
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
        # set to store the unique number
        num_set = set(nums)
        for num in num_set:
            # if num - 1 is in the set, num is not the head of a consecutive sequence
            if num - 1 not in num_set:
                cur = num
                cur_len = 1
                # if num + 1 is in the set, num is the head of a consecutive sequence
                while cur + 1 in num_set:
                    cur += 1
                    cur_len += 1
                ret = max(ret, cur_len)
        return ret
        #Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.