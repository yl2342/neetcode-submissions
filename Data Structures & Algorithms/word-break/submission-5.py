class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # solve the problem from the end of the string toward the start
        # dp[i] means whether substring s[i:] can be segmented
        # base case: dp[len(s)] = true (emptry string is valid)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if (i+len(w)) <= n and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break # break this for w in wordDict for loop
                    # The break stops the loop the moment dp[i] becomes True, 
                    # so no later word can overwrite it. 
                    # Once a position is known to be reachable, nothing else matters.
                    # It also saves time, since the remaining words aren’t tried. 
                    # But correctness is the main reason, not speed.
        return dp[0]
        