class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp number of ways to form amount a using coins processed so far
        dp = [0] * (amount + 1)
        dp[0] = 1 # exactly one way to achieve amount 0
        for i in range(len(coins)-1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            for a in range(1, amount + 1):
                # # dp[a] is the ways to make a without this coin, skip this coins
                nextDP[a] = dp[a] 
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]
        