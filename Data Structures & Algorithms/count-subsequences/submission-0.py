class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(i, j):
            if j == len(t):
                return 1 # end of t
            if i == len(s):
                return 0 # not end of t but end of s already
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                # more available i potentially
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j) 
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]
        return dfs(0,0)


        