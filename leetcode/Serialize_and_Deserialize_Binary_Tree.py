class Codec:
    #approach
    #1. use recursion to serialize and deserialize a binary tree
    #time complexity
    #1. O(n) where n is the number of nodes
    #space complexity
    #1. O(n) where n is the number of nodes

    def serialize(self, root):
        res = {}
        def serih(root,index):
            if root == None:
                return
            res[index] = root.val
            serih(root.left,2*index+1)
            serih(root.right,2*index+2)
        serih(root,0)
        return str(res)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        mapping = eval(data)
        def deserih(index):
            if index not in mapping:
                return None
            child = TreeNode(mapping[index])
            child.left = deserih(2*index+1)
            child.right = deserih(2*index+2)
            return child
        return deserih(0)
        
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        

