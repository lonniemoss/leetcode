class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
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
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
        #Given two strings text1 and text2, return the length of their longest common subsequence.
        #A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
        #If there is no common subsequence, return 0.
        #Example 1:
        #Input: text1 = "abcde", text2 = "ace" 
        #Output: 3  
        #Explanation: The longest common subsequence is "ace" and its length is 3.
        #Example 2:
        #Input: text1 = "abc", text2 = "abc"
        #Output: 3
        #Explanation: The longest common subsequence is "abc" and its length is 3.
        #Example 3:
        #Input: text1 = "abc", text2 = "def"
        #Output: 0
        #Explanation: There is no such common subsequence, so the result is 0.
        #Constraints:
        #1 <= text1.length <= 1000
        #1 <= text2.length <= 1000
        #The input strings consist of lowercase English characters only.