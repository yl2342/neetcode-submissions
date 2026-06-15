class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        if len(prices) < 2:
            return 0
        # buy, sell
        b, s = 0,1
        mp = 0
        while s < len(prices):
            if prices[b] < prices[s]:
                p = prices[s] - prices[b]
                mp = max(mp, p)
            else:
                b = s
            s += 1
        return mp



        