class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search problem
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # determine if in left sorted portion
            if nums[l] <= nums[m]:
                if nums[m] < target or target < nums[l]:
                    l = m + 1 # search right
                else:
                    r = m - 1 # search left
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1 # search left
                else:
                    l = m + 1
        return -1

        