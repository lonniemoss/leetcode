class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #approach
        #1. use two pointers to compare the characters
        #2. if the character is not a letter or a number, skip it
        #3. if the characters are not equal, return False
        #4. otherwise, return True
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
        ret = True
        # left pointer
        left = 0
        # right pointer
        right = len(s) - 1
        # loop through the string
        while left < right:
            # if the character is not a letter or a number, skip it
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            # if the characters are not equal, return False
            if s[left].lower() != s[right].lower():
                ret = False
                break
            # otherwise, move the pointers
            else:
                left += 1
                right -= 1
        return ret
        #Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.