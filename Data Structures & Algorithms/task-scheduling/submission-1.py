class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)
        q = deque() # paris of values [-count, time to unlock]
        time = 0
        # while still task left
        while maxHeap or q:
            time += 1
            if maxHeap:
                count_left = 1 + heapq.heappop(maxHeap)
                if count_left:
                    q.append([count_left, time + n])
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time




        