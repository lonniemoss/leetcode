class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #approach
        #1. use a dictionary to store the sorted string and its anagrams
        #2. add the string to the dictionary
        #3. return the values of the dictionary
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
        ret = []
        # dictionary to store the sorted string and its anagrams
        anagram_dict = {}
        # add the string to the dictionary
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagram_dict:
                anagram_dict[sorted_s] = [s]
            else:
                anagram_dict[sorted_s].append(s)
        # return the values of the dictionary
        for k in anagram_dict:
            ret.append(anagram_dict[k])
        return ret
        #Given an array of strings strs, group the anagrams together. You can return the answer in any order.