class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRS = [[1,0], [-1,0], [0,1], [0,-1] ]

        def dfs(r,c):
            # only apply on cell on edge
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                board[r][c] != "O"):
                return 
            board[r][c] = "T" # rewrite as temoparay
            for dr, dc in DIRS:
                dfs(r + dr, c + dc)
        
        # by rows
        for r in range(ROWS):
            # first colum
            if board[r][0] == "O":
                dfs(r,0)
            # last colum
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)
        
        # by cols
        for c in range(COLS):
            # first colum
            if board[0][c] == "O":
                dfs(0,c)
            # last colum
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c)

        # once edged connected O becomes T
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                else:
                    continue


        
            



        

        