class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source BFS
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[1,0], [-1,0], [0,1], [0,-1]]
        q = deque() # store rotten
        fresh = 0
        time = 0

        # locate the multi source
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c)) # rotten -> neighbour
        
        # start BFS
        while q and fresh > 0:
            # for each time, rotten ones start infecting
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r+dr, c+dc # neighbour
                    if (nr in range(ROWS) and nc in range(COLS) and
                        grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr,nc)) # add neigubour
                        fresh -= 1 
            time += 1
            
        return time if fresh == 0 else -1

            



                    


        