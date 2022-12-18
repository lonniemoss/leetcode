class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #approach
        #1. use recursion to find the level order traversal of a binary tree
        #time complexity
        #1. O(n) where n is the number of nodes
        #space complexity
        #1. O(n) where n is the number of nodes
        self.level = 0
        self.levels = []
        self.helper(root)
        return self.levels
    def helper(self, root):
        if not root:
            return
        if self.level == len(self.levels):
            self.levels.append([])
        self.levels[self.level].append(root.val)
        self.level += 1
        self.helper(root.left)
        self.helper(root.right)
        self.level -= 1
#         #Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#         #Example 1:
#         #Input: root = [3,9,20,null,null,15,7]
#         #Output: [[3],[9,20],[15,7]]