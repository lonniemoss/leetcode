class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #approach
        #1. use a dictionary to store the character and its frequency
        #2. use two pointers to keep track of the longest substring
        #3. if the character is in the dictionary, move the left pointer to the right
        #4. if the character is not in the dictionary, move the right pointer to the right
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
        ret = ""
        # dictionary to store the character and its frequency
        char_dict = {}
        # left and right pointer
        left = right = 0
        # add the character in t to the dictionary
        for c in t:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
        # count the number of characters that need to be replaced
        count = len(t)
        while right < len(s):
            # if the character is in the dictionary, add 1 to the frequency and move the right pointer
            if s[right] in char_dict:
                char_dict[s[right]] -= 1
                if char_dict[s[right]] >= 0:
                    count -= 1
            # move the right pointer
            right += 1
            # if all the characters in t have been found, move the left pointer
            while count == 0:
                # update the return value
                if not ret or right - left < len(ret):
                    ret = s[left:right]
                # if the character is in the dictionary, remove 1 from the frequency and move the left pointer
                if s[left] in char_dict:
                    char_dict[s[left]] += 1
                    if char_dict[s[left]] > 0:
                        count += 1
                # move the left pointer
                left += 1
        return ret
        #Given two strings s and t of lengths m and n respectively, return the minimum window