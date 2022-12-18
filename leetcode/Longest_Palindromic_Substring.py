class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #approach
        #1. use two pointers to compare the characters
        #2. if the characters are not equal, return False
        #3. otherwise, return True
        #time complexity
        #1. O(n) where n is the length of the string
        #space complexity
        #1. O(1)
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = ""
        # loop through the string
        for i in range(len(s)):
            # odd length
            tmp = self.helper(s, i, i)
            if len(tmp) > len(ret):
                ret = tmp
            # even length
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(ret):
                ret = tmp
        return ret
    def helper(self, s, left, right):
        # loop through the string
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
        #Given a string s, return the longest palindromic substring in s.