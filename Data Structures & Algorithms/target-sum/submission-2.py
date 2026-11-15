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




        # # top down with memoization
        # dp = {} # (index, total) -> # of ways
        # def backtrack(i, total):
        #     # total: sum up to index i (including i)
        #     if i == len(nums):
        #         return 1 if total == target else 0
        #     if (i, total) in dp:
        #         return dp[(i, total)]
        #     dp[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
        #     return dp[(i, total)]
        # return backtrack(0, 0)
           





        


        