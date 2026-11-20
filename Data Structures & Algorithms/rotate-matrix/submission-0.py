class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for d in range(r - l):
                t, b = l, r # top / bottom
                # safe the top left
                top_left = matrix[t][l + d]
                # do it backward
                # move bottom left into to left
                matrix[t][l + d] = matrix[b - d][l]
                # move bottom right to bottom left
                matrix[b - d][l] = matrix[b][r - d]
                # move top right to bottom right
                matrix[b][r - d] = matrix[t + d][r]
                # move top left to top right
                matrix[t + d][r] = top_left
            r -= 1
            l += 1


        