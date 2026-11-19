class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) # first sort by start 
        output = [intervals[0]]
        for curr_start, curr_end in intervals[1:]:
            last_end = output[-1][1]
            if curr_start <= last_end:
                output[-1][1] = max(curr_end, last_end)
            else:
                output.append([curr_start, curr_end])
        return output

        