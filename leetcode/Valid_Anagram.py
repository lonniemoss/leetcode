class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #approach
        #1. use a dictionary to store the character and its frequency
        #2. add the character in s to the dictionary
        #3. remove the character in t from the dictionary
        #4. if the dictionary is empty, return True
        #5. otherwise, return False
        #time complexity
        #1. O(n) where n is the length of the string
        #space complexity
        #1. O(n) where n is the length of the string
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = True
        # dictionary to store the character and its frequency
        char_dict = {}
        # add the character in s to the dictionary
        for c in s:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
        # remove the character in t from the dictionary
        for c in t:
            if c not in char_dict:
                ret = False
                break
            else:
                char_dict[c] -= 1
                if char_dict[c] == 0:
                    del char_dict[c]
        # if the dictionary is not empty, return False
        if char_dict:
            ret = False
        return ret
        #Given two strings s and t, return true if t is an anagram of s, and false otherwise.