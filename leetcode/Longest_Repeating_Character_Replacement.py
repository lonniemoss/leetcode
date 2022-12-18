class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
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
        ret = 0
        # dictionary to store the character and its frequency
        char_dict = {}
        # left and right pointer
        left = right = 0
        while right < len(s):
            # if the character is not in the dictionary, add it to the dictionary and move the right pointer
            if s[right] not in char_dict:
                char_dict[s[right]] = 1
            # if the character is in the dictionary, add 1 to the frequency and move the right pointer
            else:
                char_dict[s[right]] += 1
            # move the right pointer
            right += 1
            # if the number of characters that need to be replaced is greater than k, move the left pointer
            while right - left - max(char_dict.values()) > k:
                char_dict[s[left]] -= 1
                left += 1
            # update the return value
            ret = max(ret, right - left)
        return ret
        #Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.
        #In one operation, you can choose any character of the string and change it to any other uppercase English character.
        #Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.
        #Note:
        #Both the string's length and k will not exceed 104.
        #Example 1:
        #Input:
        #s = "ABAB", k = 2