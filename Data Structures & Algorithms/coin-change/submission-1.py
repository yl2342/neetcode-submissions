class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # build answers from smaller amounts to larger ones.
        # If we know the minimum coins to make a - coin
        # then we can make a using 1 extra coin.
        # So each amount depends on previously solved smaller amounts.

        
        dp = [amount +1] * (amount + 1) # use amount + 1 as inf/inpossible placeholder
        # where dp[a] = minimum coins needed to make amount a
        dp[0] = 0 # 0 coins to make amount 0

        for a in range(1, amount +1):
            for c in coins:
                if a - c >= 0:
                    # using this coin c (* 1)
                    # try to find the min coins needed for amout a-c: dp[a-c]
                    # then the min coins needed to this amount is dp[a-c] +1
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != (amount +1) else -1



        