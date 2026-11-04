class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [[1,0], [-1,0], [0,1],[0,-1]]
        visited = set()

        def dfs(r, c):
            # base case
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                grid[r][c] == 0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            res = 1
            for dr, dc in DIRS:
                res += dfs(r+dr, c+dc)
            return res
            # return (1 + dfs(r + 1, c) +
            #             dfs(r - 1, c) +
            #             dfs(r, c + 1) +
            #             dfs(r, c - 1))
        
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area

        