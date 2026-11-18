class Solution:
    def canJump(self, nums: List[int]) -> bool:




        # dp solution
        n = len(nums)
        dp = [False] * n # dp[i] is last index is reachable from index i
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            end = min(n-1, i+ nums[i]) # end index to determine range
            for j in range(i, end + 1):
                if dp[j]:
                    dp[i] = True
                    # break
        return dp[0]
                


        