# python basics:
# Sets and dicts: adding or removing elements while looping raises a RuntimeError (“Set changed size during iteration” or “dictionary changed size during iteration”). The check is on size, so changing a dict’s values for keys that already exist is fine, since the size doesn’t change.

# Lists: Python doesn’t raise an error, which is arguably worse because the behavior is quietly weird.

# Rule of thumb: don’t change the size of a collection while looping over it. Either loop over a copy (for t in list(dp):) or build a new collection, like nextDP.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        # dp[j]: whether sum j is achievable using numbers processed so far
        dp = [False] * (target + 1)
        # Before any numbers, only the empty subset exists, which sums to 0. 
        # So dp[0] = True and everything else is False
        dp[0] = True

        for num in nums:
            for j in range(target, num-1, -1):
                # For each number in nums, every sum j is reachable if :
                # 1. it was already reachable (skip num) or 
                # 2. if j - num was reachable (take num).
                dp[j] = dp[j] or dp[j - num]
                if dp[target]:
                    return dp[target]
        return dp[target]

        













        