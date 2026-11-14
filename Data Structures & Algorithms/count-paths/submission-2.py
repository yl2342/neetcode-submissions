class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # dp[m-1][n-1] = 0
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #          dp[i][j] += dp[i+1][j] + dp[i][j+1] # avoid overwrite the seed dp[m-1][n-1]
        # return dp[0][0]
        dp = [[0] * n for _ in range(m)]
        dp[-1] = [1] * n
        for row in dp:
            row[-1] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

        