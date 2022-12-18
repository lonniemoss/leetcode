class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #approach
        #1. use recursion to find the maximum depth
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
        # return the maximum depth
        return self.helper(root)
    def helper(self, root):
        # return 0 if the root is None
        if not root:
            return 0
        # return the maximum depth
        return max(self.helper(root.left), self.helper(root.right)) + 1
        #Given the root of a binary tree, return its maximum depth.
        #A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.