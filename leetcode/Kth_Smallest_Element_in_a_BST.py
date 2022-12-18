class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #approach
        #1. use recursion to find the kth smallest element in a binary search tree
        #time complexity
        #1. O(n) where n is the number of nodes
        #space complexity
        #1. O(n) where n is the number of nodes
        self.k = k
        self.kth = None
        self.helper(root)
        return self.kth
        
    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        self.k -= 1
        if self.k == 0:
            self.kth = root.val
            return
        self.helper(root.right)
        #         #Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
        #         #Example 1:
        #         #Input: root = [3,1,4,null,2], k = 1
        #         #Output: 1