class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        DIRS = [[1,0], [-1,0], [0,1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        # def dfs(r,c):
        #     if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
        #         return
        #     grid[r][c] = "0" # marked island visited
        #     for dr, dc in DIRS:
        #         dfs(r+dr, c +dc)

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             islands += 1
        # return islands


        visited = set()
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c)) # mark as vsited
            while q:
                row, col = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = row + dr, col + dc # neighbour
                    if (
                        nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
                


        
        