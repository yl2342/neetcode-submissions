"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        s, e = 0, 0
        res = 0
        meeting = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                meeting += 1
            else:
                # when start[s] = end[e], make sure march e first to end a meeting
                e += 1
                meeting -= 1
            res = max(res, meeting)
        return res




        