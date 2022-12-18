class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # flag to record if digit is removed
        flag = False
        # result list
        res = []
        # loop through the number
        for i in range(len(number)):
            # if digit is not removed and current digit is the digit to remove
            if not flag and number[i] == digit:
                # remove the digit
                flag = True
            # if digit is removed or current digit is not the digit to remove
            else:
                # append the digit to result list
                res.append(number[i])
        # if digit is not removed
        if not flag:
            # remove the last digit
            res.pop()
        # convert the result list to string and return
        return "".join(res)
        #Given a number represented as a string, remove k digits from the number so that the new number is the smallest possible.
        #The length of num is less than 10002 and will be ≥ k.
        #The given num does not contain any leading zero.
        #Example 1:
        #Input: num = "1432219", k = 3
        #Output: "1219"
        #Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
        #Example 2:
        #Input: num = "10200", k = 1
        #Output: "200"
        #Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
        #Example 3:
        #Input: num = "10", k = 2
        #Output: "0"
        #Explanation: Remove all the digits from the number and it is left with nothing which is 0.