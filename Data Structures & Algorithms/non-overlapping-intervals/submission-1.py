class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy: sort by start
        intervals.sort(key = lambda i : i[0])
        res = 0
        prev_end = intervals[0][1]
        for curr_start, curr_end in intervals[1:]:
            if curr_start  >= prev_end:
                # non- overalp 
                prev_end = curr_end
            else:
                # overlap, drop the interval with bigger end
                prev_end = min(prev_end, curr_end)
                res += 1

        return res



            




        