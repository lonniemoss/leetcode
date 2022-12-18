class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = []
        # find the first interval that is larger than newInterval
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i += 1
        # merge all overlapping intervals to one considering newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # insert the union of intervals we got
        ret.append(newInterval)
        # add all the rest
        while i < len(intervals):
            ret.append(intervals[i])
            i += 1
        return ret
        #Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
        #You may assume that the intervals were initially sorted according to their start times.