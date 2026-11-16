class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        # True dp
        # to compute row i, we only need information from:
        # the row below (i + 1) and
        # the current row as we move across columns
        # can compress and keep only one row at a time, no need the full 2D table.
        # To make this even more efficient, we ensure that s2 is the longer string
        # so the 1D array stays as small as possible.
        m, n = len(s1), len(s2)
        # assume m >= n, n is the smaller one
        if n < m:
            s1, s2 = s2, s1
            m, n = n, m
        dp = [False for _ in range(n + 1)]
        dp[n] = True
        for i in range(m, -1, -1):
            # similarly initialize
            nextDP = [False for _ in range(n + 1)]
            if i == m:
                nextDP[n] = True
            for j in range(n, -1, -1):
                if i < m and s1[i] == s3[i+j] and dp[j]:
                    nextDP[j] = True
                if j < n and s2[j] == s3[i+j] and nextDP[j + 1]:
                    # the current row as we move across columns
                    nextDP[j] = True
            dp = nextDP
        return dp[0]






        # memoization
        # dp = {} 
        # def dfs(i1, i2):
        #     if i1 == len(s1) and i2 == len(s2):
        #         return True
        #     if (i1, i2) in dp:
        #         return dp[(i1, i2)]
            
        #     if i1 < len(s1) and s1[i1] == s3[i1 + i2] and dfs(i1 + 1, i2):
        #         return True # go along s1
        #     if i2 < len(s2) and s2[i2] == s3[i1 + i2] and dfs(i1, i2 + 1):
        #         return True # go along s2
        #     dp[(i1, i2)] = False
        #     return False
        # return dfs(0,0)

        


        
        