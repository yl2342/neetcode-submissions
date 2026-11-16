class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # A (contiguous) subarray is determined by choosing a start index 
        # and an end index with start ≤ end.
        # Number of non-empty subarrays  O(n2)
        # Summing: n + (n−1) + ... + 2 + 1 = n(n+1)/2
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l,r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l,r)]
            # initialize first if not already exist
            dp[(l,r)] = 0
            # set i as the last one to burst between l and r, meaning
            # 1. everything inside [l,r] except i is already gone
            # 2. the neighbors of i are fixed
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]  # if subarray len = 1, only this line got executed
                coins += dfs(l, i - 1) + dfs(i + 1, r) # if subarray len = 1, this return 0
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        return dfs(1, len(nums) -2) # not counting neighbouring 1s
             

        