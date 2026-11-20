class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda i : i[0])
        minHeap = []
        res = {}
        i = 0
        # for sorted queries copy 
        # as queries increases, we add the interval whose start <= 1 (eligible)
        for q in sorted(queries):
            # keep adding interval to heap till 
            # 1. run out of interval
            # 2. next interval too far to the right for this query to belong to
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r)) # add size and right
                i += 1
            # pop invalid intervals that are too far to the left
            # lazy deletion: only ever care about the heap[0]
            # not al invalid intervals got poped out 
            # (some bigger-sized one remained) but okay
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
            





        