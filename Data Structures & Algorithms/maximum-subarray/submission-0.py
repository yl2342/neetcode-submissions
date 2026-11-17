class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp: each position: choice
        # 1. start new subarray at current element
        # 2. extend the subrray that end at previou index
        # dp[i] represents the maximum subaray sum starting at index x
        dp = nums.copy() # shallow copy [*nums]
        for i in range(len(nums)-2, -1, -1):
            # can leave the last element as itself consist of the maximum
            dp[i] = max(nums[i], nums[i] + dp[i+1])
        return max(dp)


            
        