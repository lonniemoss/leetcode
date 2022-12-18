class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #approach
        #1. use recursion to find the maximum path sum
        #time complexity
        #1. O(n) where n is the number of nodes
        #space complexity
        #1. O(n) where n is the number of nodes
        self.msum = float('-inf')
        self.helper(root)
        return self.msum
    def helper(self, root):
        if not root:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.msum = max(self.msum, root.val + l + r)
        return max(0, root.val + max(l, r))
#         #Given the root of a binary tree, return the maximum path sum of any path.
#         #A path is a collection of nodes that are connected by edges, where no node is connected to more than two other nodes. The path must contain at least one node and does not need to go through the root.
#         #Example 1:
#         #Input: root = [1,2,3]
#         #Output: 6
#         #Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.