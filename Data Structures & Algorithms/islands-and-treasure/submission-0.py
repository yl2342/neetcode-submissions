class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi source BFS
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        q = deque()

        def addCell(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r,c))
            q.append((r,c))
        
        # locate the multi source
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r,c))
        
        dist = 0
        while q:
            # multi source start simutaneously
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in DIRS:
                    addCell(r+dr, c+dc)
            dist += 1
        









