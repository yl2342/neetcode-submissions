class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] be the length of longest subsequence starting at index i
        # working from right to left
        n = len(nums)
        LIS = [1] * n
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # if i+1 > n , return empty range object and not execute rather
                # then raise exception
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)



        