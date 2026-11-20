class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) # +1 to work for single line
        t, b = 0, len(matrix) # +1 to work for single line
        res = []
        while l < r and t < b:
            # start spiral
            # first: move right along top edge:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            # then move down along right edge:
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            # check 
            if not (l < r and t < b):
                # already finished (1d)
                break
            # then move left along bottom edge:
            for i in range(r - 1, l - 1 , -1):
                res.append(matrix[b - 1][i])
            b -= 1
            # then move up along left edge:
            for i in range(b - 1, t - 1 , -1):
                res.append(matrix[i][l])
            l += 1
        return res

            
        