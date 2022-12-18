class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        #approach
        #1. use recursion to compare the two trees
        #time complexity
        #1. O(n) where n is the number of nodes
        #space complexity
        #1. O(n) where n is the number of nodes
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = []
        # return the result
        return self.helper(p, q)
    def helper(self, p, q):
        # if both p and q are None, return True
        if not p and not q:
            return True
        # if p and q are not None, compare the values
        if p and q:
            return p.val == q.val and self.helper(p.left, q.left) and self.helper(p.right, q.right)
        # otherwise, return False
        return False
        #Given the roots of two binary trees p and q, write a function to check if they are the same or not.
        #Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.