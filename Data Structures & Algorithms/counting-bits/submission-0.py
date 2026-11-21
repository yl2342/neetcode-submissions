class Solution:
    def countBits(self, n: int) -> List[int]:
        # dynamic programming 
        # observation Numbers repeat their bit patterns -
        # every time we reach a power of two
        # When a number is a power of two, it has exactly one 1 bit
        # the number of set bits in i is:
        # 1 (for the highest power of two) + number of set bits in the remainder
        dp = [0] * (n + 1) # dp[i]  store the number of set bits in i
        offset = 1 # most significant bit we 've reached so far
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp


        