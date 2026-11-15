class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp: possible sum: number of ways to form that sum
        # use defaultdict to access not yet added key/value pair: default = 0
        # key not bounded by range
        dp = defaultdict(int) 
        dp[0] = 1 # basecase: exactly one way to reach sum 0 before using any num
        for num in nums:
            next_dp = defaultdict(int)
            for total, count in dp.items():
                next_dp[total - num] += count
                next_dp[total + num] += count
            dp = next_dp
        return dp[target]


        


        