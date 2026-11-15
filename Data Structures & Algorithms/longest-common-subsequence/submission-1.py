class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]: LCS length for substrings text1[i:] and text2[j:]
        t1 = len(text1)
        t2 = len(text2)
        # initalize as 0 (t1 * t2 )
        dp = [[0 for _ in range(t2 + 1)] 
                 for _ in range(t1 + 1)]


        for i in range(t1 - 1, -1, -1):
            for j in range(t2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # go diagonally
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) # go right/down
        return dp[0][0]


        