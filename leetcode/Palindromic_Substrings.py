class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #approach
        #1. use two pointers to compare the characters
        #2. if the characters are not equal, return False
        #3. otherwise, return True
        #time complexity
        #1. O(n) where n is the length of the string
        #space complexity
        #1. O(1)
        N = len(s)
        ans = 0
        for center in xrange(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
        #Given a string s, return the number of palindromic substrings in it.
        #A string is a palindrome when it reads the same backward as forward.
        #A substring is a contiguous sequence of characters within the string.
        #Example 1:
        #Input: s = "abc"
        #Output: 3
        #Explanation: Three palindromic strings: "a", "b", "c".