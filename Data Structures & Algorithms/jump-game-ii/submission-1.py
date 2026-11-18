class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp version
        n = len(nums)
        dp = [float("inf")] * n  # dp[i], min jumps needed to reach n-1 from i
        dp[n - 1] = 0
        for i in range(n - 2, -1, -1):
            end = min(n - 1, i + nums[i])  
            for j in range(i, end + 1):
                # reachable range: + 1 step to j
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]

        