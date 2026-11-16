class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        LIS = -1 
        dp = {} # (r, c) -> LIP
        def dfs(r, c, prev_val):
            nonlocal LIS
            # base case 
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                matrix[r][c] <= prev_val):
                return 0
            # check memo
            if (r, c) in dp:
                return dp[(r,c)]
            res = 1
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))
                LIS = max(LIS, res) # global LIS
            # store memo 
            dp[(r,c)] = res
            return dp[(r,c)]
        # run dfs
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c , -1)
        return LIS
        



        