class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #approach
        #1. use a stack to store the left parentheses
        #2. if the character is a left parentheses, push it to the stack
        #3. if the character is a right parentheses, pop the stack
        #4. if the stack is empty, return False
        #5. if the stack is not empty, return True
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
        # dictionary to store the left parentheses and its right parentheses
        parentheses_dict = {'(':')', '{':'}', '[':']'}
        # stack to store the left parentheses
        stack = []
        # loop through the string
        for c in s:
            # if the character is a left parentheses, push it to the stack
            if c in parentheses_dict:
                stack.append(c)
            # if the character is a right parentheses, pop the stack
            else:
                if not stack:
                    ret = False
                    break
                else:
                    left_parentheses = stack.pop()
                    if parentheses_dict[left_parentheses] != c:
                        ret = False
                        break
        # if the stack is not empty, return False
        if stack:
            ret = False
        return ret
        #Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.