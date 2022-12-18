class Solution:
    
    #given the root of a binary  tree. Check whether it is a BST or not.

    #Note: We are considering that BSTs can not contain duplicate Nodes.
    #A BST is defined as follows:
    #The left subtree of a node contains only nodes with keys less than the node's key.
    #The right subtree of a node contains only nodes with keys greater than the node's key.
    #Both the left and right subtrees must also be binary search trees.

    #approach
    #1. use recursion to find the words in the board
    #time complexity
    #1. O(n) where n is the number of words
    #space complexity
    #1. O(n) where n is the number of words


    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        # code here
        return self.isBSTUtil(root, float('-inf'), float('inf'))

    def isBSTUtil(self, root, min, max):

        # Base condition
        if root is None:
            return True

        # if the node's data is less than min or greater than max
        # then return false
        if root.data < min or root.data > max:
            return False

        # recursively check left and right subtrees with updated range
        return self.isBSTUtil(root.left, min, root.data - 1) and self.isBSTUtil(root.right, root.data + 1, max)
