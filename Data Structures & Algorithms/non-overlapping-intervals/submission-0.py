class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda interval: interval[0])
        curr_interval = sorted_intervals[0]
        counter = 0
        for interval in sorted_intervals[1:]:
            if curr_interval[1] > interval[0]:
                if interval[1] < curr_interval[1]:
                    counter += 1
                    curr_interval = interval
                else:
                    counter += 1
            else:
                curr_interval = interval
        return counter