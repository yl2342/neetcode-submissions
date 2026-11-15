class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp number of ways to form amount a using coins processed so far
        dp = [0] * (amount + 1)
        dp[0] = 1 # base case: exactly one way to achieve amount 0
        for i in range(len(coins)-1, -1, -1):
            # nextDP = [0] * (amount + 1)
            # nextDP[0] = 1
            for a in range(1, amount + 1):
                #  dp[a] is the ways to make a without this coin, skip this coins
                # nextDP[a] = dp[a] 
                if a - coins[i] >= 0:
                    # nextDP[a] += nextDP[a - coins[i]]
                    dp[a] += dp[a - coins[i]]
            # dp = nextDP
        return dp[amount]

# 1d optimized: We can use one array because each new cell nextDP[a] needs only two things: the old value at the same index (dp[a]) and a new value at a smaller index (nextDP[a - coin]). The old value at index a is never needed again once nextDP[a] is computed, so it can be overwritten in place. And if we sweep upward, the smaller index a - coin has already been updated by the time we reach a, so the array there already holds exactly what nextDP[a - coin] would have held. That gives dp[a] += dp[a - coin], which is the same formula as the 2D version. The sweep direction is what makes this work: going upward means the smaller cell is already new, which allows a coin to be reused. Going downward would leave it old, so each coin could be used at most once, which is the 0/1 knapsack case.

        