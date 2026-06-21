class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums sorted
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2 # mid index
            if nums[m] < target:
                l += 1
            elif nums[m] > target:
                r -= 1
            else:
                return m
        return -1
        