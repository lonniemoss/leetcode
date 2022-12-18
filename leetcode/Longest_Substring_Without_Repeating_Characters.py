class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #approach
        #1. use a set to store the unique character
        #2. use two pointers to keep track of the longest substring
        #3. if the character is in the set, move the left pointer to the right
        #4. if the character is not in the set, move the right pointer to the right
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
        # set to store the unique character
        char_set = set()
        # left and right pointer
        left = right = 0
        while right < len(s):
            # if the character is not in the set, add it to the set and move the right pointer
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                ret = max(ret, right - left)
            # if the character is in the set, remove the character at the left pointer and move the left pointer
            else:
                char_set.remove(s[left])
                left += 1
        return ret
        #Given a string s, find the length of the longest substring without repeating characters.
        #Example 1:
        #Input: s = "abcabcbb"
        #Output: 3
        #Explanation: The answer is "abc", with the length of 3.
        #Example 2:
        #Input: s = "bbbbb"
        #Output: 1
        #Explanation: The answer is "b", with the length of 1.
        #Example 3:
        #Input: s = "pwwkew"
        #Output: 3
        #Explanation: The answer is "wke", with the length of 3.
        #Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        #Example 4:
        #Input: s = ""
        #Output: 0
        #Constraints:
        #0 <= s.length <= 5 * 104
        #s consists of English letters, digits, symbols and spaces.
        