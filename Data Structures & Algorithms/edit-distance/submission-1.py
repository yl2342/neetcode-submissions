class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            m, n = n, m
            word1, word2 = word2, word1
        # bottom up 1-d space optmized version, 
        dp = [(n - j) for j in range(n + 1)] # use the shorter one
        for i in range(m - 1, -1, -1):
            curr_dp = [float("inf") for j in range(n + 1)]
            curr_dp[n] = m - i 
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    curr_dp[j] = dp[j+1] 
                else:
                    # dp now act like the last (below/bottom) dp row close to currDP
                    curr_dp[j] = 1 + min(
                        dp[j+1], # replace
                        dp[j], # move, equal to i+1
                        curr_dp[j+1], # insert
                    )
            dp = curr_dp
        return dp[0]





        # # 2d version:
        # cache minimum number of operations to convert word1[i:] into word2[j:]
        # cache = [[float("inf") for _ in range(n + 1)]
        #          for _ in range(m + 1)]
        # # initialize 
        # for i in range(m + 1):
        #     # when word2 is at empty index
        #     cache[i][n] = m - i
        # for j in range(n + 1):
        #     cache[m][j] = n - j
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if word1[i] == word2[j]:
        #             # no operation needed
        #             cache[i][j] = cache[i + 1][j + 1]
        #         else:
        #             # replace: i+1, j+1
        #             # insert: i, j+1
        #             # remove: i+1, j
        #             cache[i][j] = 1+ min(
        #                 cache[i + 1][j + 1], 
        #                 cache[i][j + 1], 
        #                 cache[i + 1][j]
        #             )
        # return cache[0][0]
                                         


        
        