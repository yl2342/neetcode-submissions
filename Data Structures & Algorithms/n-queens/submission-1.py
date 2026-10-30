class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        posDiag = set() # upper right, r+c
        negDiag = set() # bottom right, r-c

        res = []
        board = [["."] * n for i in range(n)]

        # iterate row
        def backtrack(r):
            # base case
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                # put queen
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                # put queen
                board[r][c] = "."

        backtrack(0)

        return res





        