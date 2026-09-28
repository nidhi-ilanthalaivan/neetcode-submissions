class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda interval: interval[0])
        curr_interval = sorted_intervals[0]
        final_intervals = []
        for interval in sorted_intervals[1:]:
            if curr_interval[1] >= interval[0]:
                curr_interval[1] = max(curr_interval[1], interval[1])
            else:
                final_intervals.append(curr_interval)
                curr_interval = interval

        final_intervals.append(curr_interval)
        return final_intervals        