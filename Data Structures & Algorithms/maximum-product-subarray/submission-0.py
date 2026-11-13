# Kadane’s algorithm finds the maximum sum of a contiguous subarray in O(n) time and O(1) space. For [-2, 1, -3, 4, -1, 2, 1, -5, 4], the best subarray is [4, -1, 2, 1], with sum 6.
# The idea: Walk through the array once. At each element, you only have two choices:
# 1. Extend the best subarray that ended at the previous element.
# 2. Start fresh at the current element.
# You extend when the running sum so far helps, and you start fresh when it would only drag you down. In other words, a negative running sum is dead weight, so drop it.
# For example
# def maxSubArray(nums):
#     cur = nums[0] # best sum of a run ending here
#     best = nums[0] # best: best sum seen anywhere
#     for x in nums[1:]:
#         cur = max(x, cur + x)   # start fresh, or extend
#         best = max(best, cur)   # track the best seen anywhere
#     return best

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res
        










        