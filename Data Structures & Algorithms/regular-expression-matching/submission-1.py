class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # bottom up
        m, n = len(s), len(p)
        dp = [False for _ in range(n + 1)]
        dp[n] = True
        for i in range(m, -1, -1):
            # start from m: (e.g. "" vs a*)
            # Empty string vs. remaining pattern is a real case 
            curr_dp = [False for _ in range(n + 1)]
            curr_dp[n] = (i == m)
            for j in range(n - 1, -1, -1):
                match = i < m and (s[i] == p[j] or p[j] == ".")
                if j < (n - 1) and p[j + 1] == "*":
                    # option 1: skip x*, zero occurrence
                    curr_dp[j] = curr_dp[j + 2]
                    # option 2: if match, consume 1 char from s and stay on j
                    if match:
                        curr_dp[j] = curr_dp[j] or dp[j]
                elif match:
                    # Otherwise (no *) match move both forward 
                    # use dp means the botton row, use j+1 mean use the right column
                    # same as dp[i+1][j+1]
                    curr_dp[j] = dp[j+1]
            dp = curr_dp
        return dp[0]
                        


    

        # # top down dp:
        # 
        # cache = {}
        # def dfs(i, j):
        #     if j == n:
        #         return i == m
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     match = (i < m) and (s[i] == p[j] or p[j] == ".")
        #     if (j + 1) < n and p[j+1] == "*":
        #         # skip *  or use *
        #         cache[(i, j)] = (
        #             dfs(i, j + 2) or 
        #             (match and dfs(i + 1, j))
        #         )
        #         return cache[(i, j)]
        #     if match: 
        #         cache[(i, j)] = dfs(i + 1, j + 1)
        #         return cache[(i, j)]
        #     cache[(i, j)] = False
        #     return cache[(i, j)]
        # return dfs(0, 0)
        