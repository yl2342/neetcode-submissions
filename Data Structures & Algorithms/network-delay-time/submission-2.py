class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm (using minHeap)
        # Python’s standard library gives you heapq, a min-heap built on a plain list.
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append([v, w])
        minheap = [[0, k]] # weight (sort by weight), node, initialized with specified args
        visit = set()
        t = 0
        while minheap:
            # current/sofar
            w_cur, n_cur = heapq.heappop(minheap) # weight w is accumulated
            if n_cur in visit:
                continue
            visit.add(n_cur)
            t = w_cur

            # neighbour
            for n_nei, w_nei in edges[n_cur]:
                if n_nei not in visit:
                    heapq.heappush(minheap,[w_cur + w_nei, n_nei])
        
        return t if len(visit) == n else -1



        