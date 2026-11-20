class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # left to right, top to bottom
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False
        # determin which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0 
                    else:
                        rowZero = True # use for rows
        # address the inner subset grid (n-1 * n-1)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        # address the top/left edges
        if matrix[0][0] == 0:
            # col[0]
            for r in range(ROWS):
                matrix[r][0] = 0
        if rowZero:
            # row[0] should be zero out
            for c in range(COLS):
                matrix[0][c] = 0
            



        


        
        