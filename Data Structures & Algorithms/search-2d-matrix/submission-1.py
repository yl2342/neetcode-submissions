class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        t, b = 0, rows-1 # top and bottom pointer 
        # binary serach for row range
        while t <= b:
            m0 = (t + b) // 2
            if target > matrix[m0][-1]:
                t = m0 + 1
            elif target < matrix[m0][0]:
                b = m0 - 1
            else:
                break # with m found

        if not t <= b:
            return False # out of bound
        # binary search for selected row
        l, r = 0, cols-1 
        while l <= r:
            m1 = (l + r) // 2
            if target > matrix[m0][m1]:
                l = m1 + 1
            elif target < matrix[m0][m1]:
                r = m1 - 1
            else:
                return True
        return False


        
        


        