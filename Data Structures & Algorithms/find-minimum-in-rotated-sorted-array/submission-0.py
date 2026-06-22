class Solution:
    def findMin(self, nums: List[int]) -> int:
        # hint: sorted + logn -> binary search
        
        l, r = 0, len(nums)-1
        # nums[r] is always a safe anchor — the minimum is always ≤ nums[r], so you never accidentally discard it.
        # When nums[m] < nums[r], m itself could be the minimum. So keep m in the search window with r = m. (Setting r = m - 1 would skip it.) - This also explains the loop condition l < r (not l <= r) — once they meet, you've found it.
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m # m still could be the min
            else:
                l = m + 1
        return nums[l] # lower bound





        # res = nums[0]
        # while l <= r:
        #     # finally be in a left-side sorted subsection
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     m = (l + r) // 2
        #     res = min(res, nums[m])
        #     # if in left sorted order, go to right part
        #     # basically try to find the pivot point
        #     if nums[l] <= nums[m]:
        #         l = m + 1
        #     else:
        #         r = m -1
        # return res

                

        
        