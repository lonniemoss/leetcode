class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        # return list
        ret = 0
        # sort the list by the start time
        intervals.sort(key = lambda x : x[0])
        # get the first end time
        end = intervals[0][1]
        # traverse the list
        for i in range(1, len(intervals)):
            # if the current start time is less than the previous end time
            if intervals[i][0] < end:
                # if the current end time is less than the previous end time
                if intervals[i][1] < end:
                    # update the end time
                    end = intervals[i][1]
                # count the number of overlapping intervals
                ret += 1
            # if the current start time is greater than the previous end time
            else:
                # update the end time
                end = intervals[i][1]
        return ret
        #Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.