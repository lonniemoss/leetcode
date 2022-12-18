class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #approach
        #1. use recursion to invert the tree
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
        # return the inverted tree
        return self.helper(root)
    def helper(self, root):
        # return None if the root is None
        if not root:
            return None
        # swap the left and right
        root.left, root.right = root.right, root.left
        # invert the left and right
        self.helper(root.left)
        self.helper(root.right)
        # return the root
        return root
        #Given the root of a binary tree, invert the tree, and return its root.
        #Example 1:
        #Input: root = [4,2,7,1,3,6,9]
        #Output: [4,7,2,9,6,3,1]
        #Example 2:
        #Input: root = [2,1,3]
        #Output: [2,3,1]
        #Example 3:
        #Input: root = []
        #Output: []
        #Constraints:
        #The number of nodes in the tree is in the range [0, 100].
        #-100 <= Node.val <= 100