class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            prev2, prev1 = 0, 0
            for num in nums:
                prev2, prev1 = prev1, max(prev2 + num, prev1)
            return prev1
        return max(nums[0], helper(nums[1:]), helper(nums[:(len(nums)-1)]))
        