from lib2to3.pytree import Node


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # return node
        retNode = None
        # visited node
        visited = {}
        # queue
        queue = []
        # if node is None
        if node is None:
            return retNode
        # add node to queue
        queue.append(node)
        # add node to visited
        visited[node] = Node(node.val, [])
        # while queue is not empty
        while queue:    
            # get node from queue
            n = queue.pop(0)
            # for each neighbor
            for neighbor in n.neighbors:
                # if neighbor is not visited
                if neighbor not in visited:
                    # add neighbor to queue
                    queue.append(neighbor)
                    # add neighbor to visited
                    visited[neighbor] = Node(neighbor.val, [])
                # add neighbor to visited[n]
                visited[n].neighbors.append(visited[neighbor])
        # return visited[node]
        return visited[node]
        #Given a reference of a node in a connected undirected graph.
        #
        #Return a deep copy (clone) of the graph.
        #
        #Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
        #Each neighbor
        #Example:
        #Input:
        #{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
        #Explanation:
        #Node 1's value is 1, and it has two neighbors: Node 2 and 4.
        #Node 2's value is 2, and it has two neighbors: Node 1 and 3.
        #Node 3's value is 3, and it has two neighbors: Node 2 and 4.
        #Node 4's value is 4, and it has two neighbors: Node 1 and 3.
        #Note:
        #The number of nodes will be between 1 and 100.
        #The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
        #Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
        #You must return the copy of the given node as a reference to the cloned graph.
        

        
