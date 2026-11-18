class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy
        res = 0
        l = r = 0 # range index
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            # move the range boundary pointer
            l = r + 1  # guarantee solution so no 0
            r = furthest
            res += 1
        return res






        # # dp version
        # n = len(nums)
        # dp = [float("inf")] * n  # dp[i], min jumps needed to reach n-1 from i
        # dp[n - 1] = 0
        # for i in range(n - 2, -1, -1):
        #     end = min(n - 1, i + nums[i])  
        #     for j in range(i, end + 1):
        #         # reachable range: + 1 step to j
        #         dp[i] = min(dp[i], 1 + dp[j])
        # return dp[0]

        