class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
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
        # sort the intervals by their start time
        intervals.sort(key = lambda x: x[0])
        # merge all overlapping intervals to one considering newInterval
        for i in range(len(intervals)):
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if len(ret) == 0 or ret[-1][1] < intervals[i][0]:
                ret.append(intervals[i])
            else:
                # otherwise, there is overlap, so we merge the current and
                # previous intervals.
                ret[-1][1] = max(ret[-1][1], intervals[i][1])
        return ret
        #Given a collection of intervals, merge all overlapping intervals.
        #For example,
        #Given [1,3],[2,6],[8,10],[15,18],
        #return [1,6],[8,10],[15,18].
        #Make sure the returned intervals are sorted.