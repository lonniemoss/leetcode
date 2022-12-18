class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # build graph
        graph = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        # build in-degree
        in_degree = [0] * numCourses
        for i in range(len(prerequisites)):
            in_degree[prerequisites[i][0]] += 1
        # bfs
        queue = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        while len(queue) > 0:
            node = queue.pop(0)
            for i in range(len(graph[node])):
                in_degree[graph[node][i]] -= 1
                if in_degree[graph[node][i]] == 0:
                    queue.append(graph[node][i])
        for i in range(numCourses):
            if in_degree[i] > 0:
                return False
        return True
        #There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
        #Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
        #Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?