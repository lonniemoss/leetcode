class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #approach
        #1. use recursion to construct a binary tree from preorder and inorder traversal
        #time complexity
        #1. O(n) where n is the number of nodes
        #space complexity
        #1. O(n) where n is the number of nodes
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1],inorder[:index])
        root.right = self.buildTree(preorder[index+1:],inorder[index+1:])
        return root
        #         #Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
        #         #Example 1:
        #         #Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        #         #Output: [3,9,20,null,null,15,7]