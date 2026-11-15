class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memoization
        dp = {} # key: (i, buying), value: best profit we can achieve at day i

        def dfs(i, buying):
            # recrusion
            # base case
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            # each time buy/sell, negate the buying state , think of open/close {/}
            if buying:
                # buying = True means you hold nothing and may buy
                # two choices when buying state: buy/cooldown
                # if buying: i+1 , then negate the buying state since now is buying
                # and next step need the state of not buying
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying) # cool down can step no matter what
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # buying = False means you hold a share and may sell.
                # negatie buying for transit state, not the same buying as above
                sell = dfs(i+2, not buying) + prices[i] # i+2, force one cool down
                cooldown = dfs(i+1, buying) # cool down can step no matter what
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True) 
        # maximum profit can achieve (at day 0)
        # what’s the best total profit if I’m on day 0:
        # holding nothing, and free to buy




        