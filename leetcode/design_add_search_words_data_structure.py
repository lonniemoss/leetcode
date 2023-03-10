import collections


class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        
    #approach
    #1. use a dictionary to store the words
    #2. use recursion to find the word
    #time complexity
    #1. O(n) where n is the number of words
    #space complexity
    #1. O(n) where n is the number of words

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)