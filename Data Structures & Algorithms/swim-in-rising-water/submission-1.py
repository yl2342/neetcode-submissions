class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # question reframing: what is the path we can take such the maximum height along the path is minimized
        n = len(grid)
        DIRS = [[1,0], [-1,0], [0,1],[0,-1]]
        visit = set() 
        visit.add((0,0))# lists aren’t hashable, can’t put them in a set. Use tuples.
        minheap = [(grid[0][0], 0, 0)] # initialized with own height at top left
        while minheap:
            h_cur, r_cur, c_cur = heapq.heappop(minheap) # h_cur means max heght so far
            if r_cur == n-1 and c_cur == n-1:
                return h_cur
            for dr, dc in DIRS:
                r_nei, c_nei = r_cur + dr, c_cur + dc
                if (r_nei in range(n) and c_nei in range(n) and
                    (r_nei, c_nei) not in visit):
                    visit.add((r_nei, c_nei))
                    heapq.heappush(minheap,(max(h_cur, grid[r_nei][c_nei]),r_nei, c_nei))
            



        
        